import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStramLitUi:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title= "🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())

        with st.sidebar:
            #Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            #LLM selections
            self.user_controls["selected_llm"] = st.selectbox("Selected LLM", llm_options)

            if self.user_controls["selected_llm"] == "GROQ":
                # Model selection
                model_options = self.config.get_groq_models()

                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"]=st.text_input("API Key",type="password")

                 # Validate API key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")
                
                 ## USecase selection
            self.user_controls["selected_usecase"]=st.selectbox("Select Usecases",usecase_options)
            
            if self.user_controls["selected_usecase"] == "Toolbot" :
                os.environ["TAVILY_API_KEY"]=self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"]=st.text_input("Tavily API Key",type="password")
                st.warning("⚠️ TOOL BOT requires a Tavily API key. Get one at: https://www.tavily.com/")

        return self.user_controls


    



