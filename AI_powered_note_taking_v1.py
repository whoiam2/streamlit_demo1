import streamlit as st
from streamlit_pills import pills
import base64
import os
import plotly.express as px
import pandas as pd
from streamlit_modal import Modal
import streamlit.components.v1 as components
from io import StringIO
from openai import OpenAI
from datetime import datetime
ref_link='https://notebooklm.google.com/notebook/f7607d7a-584c-4f35-96fc-f6815c573a6c?_gl=1*1xmsgc1*_ga*MTE1NzQ5NDAzMy4xNzE3Njk1NTM5*_ga_W0LDH41ZCB*MTcxNzY5NTUzOS4xLjAuMTcxNzY5NTUzOS42MC4wLjA.&original_referer=https:%2F%2Fnotebooklm.google%23'

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

@st.cache_resource()
def get_img_with_href(local_img_path, target_url):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <a href="{target_url}">
            <img src="data:image/{img_format};base64,{bin_str}" width="100%" height="20%" />
        </a>'''
    return html_code

def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    components.html(open_script)

school = 'Seminole state college of florida'
course = 'Management 3240'
# from streamlit_option_menu import option_menu
st.set_page_config(
    page_title=f"Course Hero - {course} - {school}",
    layout="wide",
    initial_sidebar_state="expanded")

def on_upload():
    st.session_state.text = note_text

def find_note_length():
    st.session_state.text = new_txt
    # note_length = len(st.session_state.text)
    # return len(note_text)
#configuring side bars
st.sidebar.header(f'Course {course} - {school}')

add_selectionbox = st.sidebar.selectbox(
    'Select a note',
    ('New note','June 20, 2024 - Midterm preparation','June 6, 2024 - study materials')
)
paraphraser_url = 'https://www.coursehero.com/tools/paraphraser/'
grammar_checker_url = 'https://www.coursehero.com/tools/grammar-checker/'
ai_test_prep_url = 'https://www.coursehero.com/ai-tutor/flashcards/'
ai_essay_url = 'https://www.coursehero.com/tools/proofreader/'


st.sidebar.write('')
st.sidebar.write('Checkout our tools below to help with your study needs!')
st.sidebar.page_link(paraphraser_url, label="Paraphraser", icon="🅿️")
st.sidebar.page_link(grammar_checker_url, label="Grammar checker", icon="🆓")
st.sidebar.page_link(ai_test_prep_url, label="AI test prep", icon="🆙")
st.sidebar.page_link(ai_essay_url, label="AI essay helper", icon="🆙")


#################################### main page asset ####################################
doc_assets = {
    1:('Assets/SUS1501_image1_Doc.png','https://www.coursehero.com/file/100814111/Assignement-2docx/'),
    2:('Assets/SUS1501_image2_Doc.png','https://www.coursehero.com/file/74192906/SUS1501-Assignment-05pdf/'),
    3:('Assets/SUS1501_image3_Doc.png','https://www.coursehero.com/file/67962013/JM-LUNGU-65933796docx/'),
    4:('Assets/SUS1501_image4_Doc.png','https://www.coursehero.com/file/33597037/SUS1501-assignment-02-S2-2018pdf/'),
    5:('Assets/SUS1501_image5_Doc.png','https://www.coursehero.com/file/55110838/SUS-Assignment-5docx/'),
    6:('Assets/SUS1501_image6_Doc.png','https://www.coursehero.com/file/22965867/Utilitarianism-is-the-best-approach-to-environmental-issues/'),
    7:('Assets/SUS1501_image7_Doc.png','https://www.coursehero.com/file/135628655/portfolio-template-3docx/'),
    8:('Assets/SUS1501_image8_Doc.png','https://www.coursehero.com/file/88996687/Assignment-05-Back-at-me-Virtue-Ethicsdoc/'),
    9:('Assets/SUS1501_image9_Doc.png','https://www.coursehero.com/file/30843691/SUS1501-Assignment-03docx/'),
}

qa_assets = {
    1:('Assets/SUS1501_image1_QA.png','https://www.coursehero.com/tutors-problems/World-History/47646324-502-SOAPS-Eyewitness-to-Execution-5-Subject-0-Occasion-A-/'),
    2:('Assets/SUS1501_image2_QA.png','https://www.coursehero.com/tutors-problems/Entrepreneurship/43570754-An-analysis-of-the-inequalities-described-using-ALL-of-John/'),
    3:('Assets/SUS1501_image3_QA.png','https://www.coursehero.com/tutors-problems/Operations-Management/40928956-Show-me-a-great-fortune-and-Ill-show-you-a-great-crime-a/'),
    4:('Assets/SUS1501_image4_QA.png','https://www.coursehero.com/tutors-problems/Business-Law/38537564-What-would-Kant-probably-have-said-about-van-Dijk-earning-ZAR-19/'),
    5:('Assets/SUS1501_image5_QA.png','https://www.coursehero.com/student-questions/33217746-1-I-didnt-join-the-struggle-to-be-poor-Smuts/'),
    6:('Assets/SUS1501_image6_QA.png','https://www.coursehero.com/file/22965867/Utilitarianism-is-the-best-approach-to-environmental-issues/'),
    7:('Assets/SUS1501_image7_QA.png','https://www.coursehero.com/student-questions/32585086-sustainability-and-greed-assignment-5-please-help-I-am/'),
    8:('Assets/SUS1501_image8_QA.png','https://www.coursehero.com/student-questions/32313861-Is-it-good-for-other-to-earn-R1-9-billion-while-other/'),
    9:('Assets/SUS1501_image9_QA.png','https://www.coursehero.com/tutors-problems/Business-Other/31915236-So-in-assignment-2-we-reflected-on-a-particular-case-involving-great/'),
}

june20_note = '''Assessment
A. BreathingPatterns:noticeifpatientappearsdyspneic,usespursedlipbreathing, andleansforwardtobreathe. Commonpatternsofbreathing:
1. Eupnea: normal 12-20 respirations
2. Cheyne-Stokes: irregular pattern seen prior to death and with narcotic overdose;
rapid respirations alternating with slow; caused by decreased responsiveness of
chemoreceptors to CO2
3. Biot's respiration: (sometimes also called ataxic respiration): abnormal pattern of
breathing characterized by groups of quick, shallow inspirations followed by regular or irregular periods of apnea. Biot's respiration is caused by damage to the medulla oblongata due to strokes or trauma.
4. Kussmaul's respirations: rapid, deep breathing. Usually compensatory for acidosis(i.e. DKA, aspirin overdose)
5. Apneusticrespiration:(a.k.a.apneusis)isanabnormalpatternofbreathing characterized by deep, gasping inspiration with a pause at full inspiration followed by a brief, insufficient release. It is caused by damage to the pons or upper medulla caused by strokes or trauma. Specifically, concurrent removal of input from the vagus nerve and the pneumotaxic center causes this pattern of breathing.
6. Hypoventilation: caused by overdose of drugs, bradypnea, NM disorders
7. Hyperventilation: tachypnea - rapid shallow ventilations- seen with lack of oxygen i.e.
pneumonia, exertion (100 yd dash)
8. Paroxysmal Nocturnal Dyspnea: PND- fluid in the body is mobilized at night when
the patient is sleeping and moves into the lung, causing SOB; associated with heart failure
B. Percussion: sound made depends on amount of tissue under area 1. Normal: Resonance (hollow, low pitch)
2. Dullness: Consolidation
3. Tympanic: Pneumothorax
4. Hyperresonance: COPD
C. Normal Breath Sounds: Assess location, pitch, quality, intensity & duration
1. Vesicular: sounds like leaves rustling and is heard over peripheral lungs
2. Bronchial: hollow sounds heard over the sternum- if heard elsewhere, it is due to
fluid or a mass underneath and is abnormal. Consolidation causes transmission of
bronchial sounds to the periphery; the lung is “solid” with water.
3. Bronchovesicular: sounds heard in-between bronchus and peripheral fields
D. Adventitious Breath Sounds
1. Crackles: popping or crackling sounds heard over the peripheral lung fields Caused by fluid in the alveoli and bronchioles'''

june6_note='''Diagnostic Tests
Formulas
dnodal = (Total) Nodal Delay
dproc = Processing Delay
dqueue = Queuing Delay
dtrans = Transmission Delay = L/R
L = Length (in bits) of the packet
R = Bits/second link bit rate
dprop = Propagation Delay = D/S
D = Distance in meters
S = Propagation speed fixed at C (speed of light)
C = 3 * 10^8 m/s
dnodal = dproc + dqueue + dtrans + dprop
dend-to-end = End to End Delay
dend-to-end (with just transmission delay) = N(L/R) = N(dtrans)
dend-to-end = N(dproc + dtrans + dprop)
N = Number of links (assume N-1 routers between source and destination)
dend-to-end (with just transmission delay, including packets) = (N + P – 1) * (L/R)
Host A transmits packet at time t = 0; at time t = dtrans the last bit of the packet would be leaving Host A but not yet propagated through the link yet as t = 0
dprop
> dtrans at time t = dtrans, the first bit of the packet would be in the link just leaving Host A but would not have yet reached Host B
dprop'''

#################################### asset end ####################################

####### end note area #######
note_text=''
st.session_state.text = note_text
# if add_selectionbox == 'New Note':
#     note_text = ''
if add_selectionbox == 'June 20, 2024 - Midterm preparation':
    # temp_note1=note_text
    st.session_state.text = june20_note
if add_selectionbox == 'June 6, 2024 - study materials':
    # temp_note2=note_text
    st.session_state.text = june6_note

text_title = f'''<h1 style='font-size:28px;'> {course} - {school}  </h1>'''
st.markdown(text_title, unsafe_allow_html=True)
st.markdown(f'''<h1 style='font-size:20px; color: blue;'> {add_selectionbox}''', unsafe_allow_html=True)
st.write(f'Last modified date: {datetime.now().replace(microsecond=0)}')

file_uploaded = st.file_uploader('Upload your current note to start or start writing in the text box below',type = ['txt','docx','doc'])
if file_uploaded is not None:
    stringio = StringIO(file_uploaded.getvalue().decode("utf-8"))
    st.session_state.text = st.session_state.text+stringio.getvalue()
    # st.session_state.text = note_text
st.button('Upload',on_click = on_upload)
reco_text_1 = 'Related materials based on your content based on your notes'
# note_length = len(st.session_state.text)
st.write(len(st.session_state.text))
if len(st.session_state.text)>10:
    if add_selectionbox not in ('June 20, 2024 - Midterm preparation','June 6, 2024 - study materials'):
        st.markdown(f'''<h1 style='color: green; font-size:20px;'>{reco_text_1} </h1>''',unsafe_allow_html=True)
        doc_factor=1
        qa_factor=-1
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                        gif_html = get_img_with_href(doc_assets[indx+doc_factor][0], doc_assets[indx+doc_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
                else:
                        gif_html = get_img_with_href(qa_assets[indx+qa_factor][0], qa_assets[indx+qa_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
    if add_selectionbox == 'June 20, 2024 - Midterm preparation':
        st.markdown(f'''<h1 style='color: green; font-size:20px;'>{reco_text_1} </h1>''',unsafe_allow_html=True)
        doc_factor=2
        qa_factor=0
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                        gif_html = get_img_with_href(doc_assets[indx+doc_factor][0], doc_assets[indx+doc_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
                else:
                        gif_html = get_img_with_href(qa_assets[indx+qa_factor][0], qa_assets[indx+qa_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)  
    if add_selectionbox == 'June 6, 2024 - study materials':
        st.markdown(f'''<h1 style='color: green; font-size:20px;'>{reco_text_1} </h1>''',unsafe_allow_html=True)
        doc_factor=2
        qa_factor=0
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                        gif_html = get_img_with_href(doc_assets[indx+doc_factor][0], doc_assets[indx+doc_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
                else:
                        gif_html = get_img_with_href(qa_assets[indx+qa_factor][0], qa_assets[indx+qa_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
if len(st.session_state.text)>10:
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    with col1:
        with st.popover('Chat with your note'):
            client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
            if "messages" not in st.session_state:
                st.session_state.messages = [{'role':'system','content':f'You are a helpful assistant, you get a note that is enclosd with <>. Prepare to answer question on it. <{st.session_state.text}>'}]
            if "openai_model" not in st.session_state:
                st.session_state["openai_model"] = "gpt-3.5-turbo"
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    if message["role"] =='system':
                        st.markdown('Welcome to our note chat! Feel free to ask me anything you are interested about!')
                    # elif message["role"] =='user':
                    #     continue
                    else:
                        st.markdown(message["content"])
            if prompt := st.chat_input("Can you quickly summarize this note?"):
                # with st.chat_message("user"):
                #     st.markdown(prompt)
                # Add user message to chat history
                st.session_state.messages.append({"role": "user", "content": prompt})
                # Display user message in chat message container
                with st.chat_message("user"):
                    st.markdown(prompt)
            with st.chat_message("assistant"):
                stream = client.chat.completions.create(
                    model=st.session_state["openai_model"],
                    # prompt = st.session_state["prompt"],
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    stream=True,
                )
                response = st.write_stream(stream)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.button('copy response to note',key='copy_response')


    with col2:
        st.button('Generate Practice Test from Notes')
    with col3:
        st.button('Generate Flash cards from Notes')
    with col4:
        st.button('Enrich Notes with AI')

new_txt = st.text_area('Your notes below:',st.session_state.text,height = 1000,key='note_area',placeholder = 'Start by uploading or enter your notes',on_change=find_note_length)
st.session_state.text = new_txt
# st.write()
# len(st.session_state.text)
# note_length = len(new_txt)
    # st.text_area('Your notes below:',note_text,height = 1000,key='note_area')
####### end note area #######

