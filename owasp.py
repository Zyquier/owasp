import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

def get_owasp_top_ten():
    url = "https://owasp.org/www-project-top-ten/"
    response = requests.get(url)
    
    if response.status_code != 200:
        return None  # Return None if the page could not be retrieved
    
    soup = BeautifulSoup(response.text, 'html.parser')
    top_ten_list = []

    # Find the section containing the top 10 risks
    risks_section = soup.find('section', {'id': 'sec-main'})
    
    if not risks_section:
        return None  # Return None if the section is not found
    
    # Find all list items (li) within the section
    risk_items = risks_section.find_all('li')
    
    for item in risk_items:
        # Safely try to extract the title and description
        try:
            title_tag = item.find('a')
            if title_tag:
                title = title_tag.text.strip()
                description = item.get_text(separator=" ").strip()
                top_ten_list.append({
                    'rank': len(top_ten_list) + 1,
                    'title': title,
                    'description': description
                })
        except Exception as e:
            print(f"Error processing item: {e}")
            continue  # Skip to the next item if there’s an error
    
    return top_ten_list

def main():
    st.title("OWASP Top Ten")
    top_ten = get_owasp_top_ten()
    
    if top_ten:
        # Create a DataFrame from the list
        df = pd.DataFrame(top_ten)
        
        # Display the DataFrame
        st.subheader("OWASP Top Ten Data")
        st.dataframe(df)
        
        # Add the download button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download as CSV",
            data=csv,
            file_name='owasp_top_ten.csv',
            mime='text/csv',
        )
    else:
        st.write("Could not retrieve the OWASP Top Ten.")

if __name__ == "__main__":
    main()

