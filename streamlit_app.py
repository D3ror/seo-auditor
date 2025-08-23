import streamlit as st, pandas as pd, json, pathlib
st.title("SEO Crawl & Indexability Auditor")
upload = st.text_input("Domain (https://example.com)")
if st.button("Run"):
    # call your crawl runner (make sure it writes to /tmp or ./data)
    st.info("Crawling… this may take a while.")
# Show latest results
p = pathlib.Path("out/results.csv")
if p.exists(): st.dataframe(pd.read_csv(p))
