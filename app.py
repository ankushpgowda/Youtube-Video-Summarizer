from youtube_transcript_api import YouTubeTranscriptApi
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")
def summarize(link):
    complete_transcript = YouTubeTranscriptApi.get_transcript(link)
    transcript =""
    for i in range(len(complete_transcript)):
        transcript = transcript + complete_transcript[i]['text'] + " "

    template = '''Question: Write a summary of the following youtube video transcript in 100 words.
    Transcript : "{transcript}" 
    '''
    prompt = PromptTemplate.from_template(template)
    llm = OpenAI()
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    return llm_chain.invoke(transcript)['text']

