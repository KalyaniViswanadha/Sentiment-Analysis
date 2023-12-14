from textblob import TextBlob
import pandas as pd
import cleantext
import streamlit as st

st.header('Sentiment Analysis')
with st.expander('Analyze Text'):
  text=st.text_input('Text Here: ')
  if text:
    blob=TextBlob(text)
    st.write('Polarity: ',round(blob.sentiment.polarity,2))
    st.write('Subjectivity: ',round(blob.sentiment.subjectivity,2))
  pre= st.text_input('Clean Text: ')
  if pre:
    st.write(cleantext.clean(pre,clean_all=False, extra_space=True,stopwords=True,
                             Lowercse=True, numbers=True, punct=True))
with st.expander('Analyze CSV'):
  upl=st.file_uploader('Upload File')

  def score(x):
    blob1=TextBlob(x)
    return blob1.sentiment.polarity

  def analyze(x):
    if x>=0.5:
      return 'Positive'
    elif x<=-0.5:
      return 'Negative'
    else:
      return 'Neutral'
  if upl:
    df=pd.read_csv(upl)
    del df['Unnamed: 0']
    df['score']=df['tweets'].apply(score)
    df['analysis']=df['score'].apply(analyze)
    st.write(df.head())

    # @st.cache

    # def convert_df(df):
    #   return df.to_csv().encode('utf-8')
    # csv=convert_df(df)
    # st.download_button(
    #     label="Download data as csv",
    #     data=csv,

    # )
