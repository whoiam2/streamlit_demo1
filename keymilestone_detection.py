import streamlit as st
import base64
import os
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
            <img src="data:image/{img_format};base64,{bin_str}" width="100%" />
        </a>'''
    return html_code
# from streamlit_option_menu import option_menu
st.set_page_config(
    page_title="Course Hero - SUSI 1501 - University of South Africa",
    layout="wide",
    initial_sidebar_state="expanded")

#configuring side bars
st.sidebar.header('Course SUS 1505 - University of South Africa')
add_selectionbox = st.sidebar.selectbox(
    'Select a semester',
    ('Spring 2024','Summer 2024','Fall 2024')
)
paraphraser_url = 'https://www.coursehero.com/tools/paraphraser/'
grammar_checker_url = 'https://www.coursehero.com/tools/grammar-checker/'
ai_test_prep_url = 'https://www.coursehero.com/ai-tutor/flashcards/'
ai_essay_url = 'https://www.coursehero.com/tools/proofreader/'
nav = st.sidebar.radio('Choose a milestone option',['Assignment - week of 2024-06-03', 'Assignment - week of 2024-06-10','Essay - week of 2024-06-17','Midterm - week of 2024-07-08','Final - week of 2024-08-19'])

st.sidebar.write('Checkout our tools below to help with your study needs!')
st.sidebar.page_link(paraphraser_url, label="Paraphraser", icon="🅿️")
st.sidebar.page_link(grammar_checker_url, label="Grammar checker", icon="🆓")
st.sidebar.page_link(ai_test_prep_url, label="AI test prep", icon="🆙")
st.sidebar.page_link(ai_essay_url, label="AI essay helper", icon="🆙")

reco_text_1 = 'Most viewed contents at this milestone.'
reco_text_2 = 'Relevant contents based on the time of the semester.'
reco_text_3 = 'Content with similar topics to most viewed content.'
#end of side bar configuration
text_to_render = f'''<h1 style='color: blue; font-size:28px;'> Start preparing for your {nav.split(' ')[0]} that is happening on the week of {nav.split(' ')[-1]}  </h1>'''
st.markdown(text_to_render, unsafe_allow_html=True)
# col1, col2 = st.columns(2)
# col1.write("This is column 1")
# col2.write("This is column 2")
if nav.split(' ')[0] == 'Assignment':
    tab1,tab2,tab3 = st.tabs(['All Content','Document','Q&A'])
    with tab1:
        tab1.markdown(f'''<h1 style='color: green; font-size:20px;'>{reco_text_1} </h1>''',unsafe_allow_html=True)
        with st.container():
            col1,col2,col3,col4=st.columns(4)
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image1_Doc.png', 'https://www.coursehero.com/file/100814111/Assignement-2docx/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image2_Doc.png', 'https://www.coursehero.com/file/74192906/SUS1501-Assignment-05pdf/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col3:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image1_QA.png', 'https://www.coursehero.com/tutors-problems/World-History/47646324-502-SOAPS-Eyewitness-to-Execution-5-Subject-0-Occasion-A-/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col4:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image2_QA.png', 'https://www.coursehero.com/tutors-problems/Entrepreneurship/43570754-An-analysis-of-the-inequalities-described-using-ALL-of-John/')
                st.markdown(gif_html, unsafe_allow_html=True)
        tab1.write('')
        tab1.markdown(f'''<h1 style='color: blue; font-size:20px;'>{reco_text_2}''',unsafe_allow_html=True)
        with st.container():
            col1,col2,col3,col4=st.columns(4)
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image3_Doc.png', 'https://www.coursehero.com/file/67962013/JM-LUNGU-65933796docx/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image4_Doc.png', 'https://www.coursehero.com/file/33597037/SUS1501-assignment-02-S2-2018pdf/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col3:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image3_QA.png', 'https://www.coursehero.com/tutors-problems/Operations-Management/40928956-Show-me-a-great-fortune-and-Ill-show-you-a-great-crime-a/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col4:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image4_QA.png', 'https://www.coursehero.com/tutors-problems/Business-Law/38537564-What-would-Kant-probably-have-said-about-van-Dijk-earning-ZAR-19/')
                st.markdown(gif_html, unsafe_allow_html=True)
        tab1.write('')
        tab1.markdown(f'''<h1 style='color: red; font-size:20px;'>{reco_text_3}''',unsafe_allow_html=True)
        with st.container():
            col1,col2,col3,col4=st.columns(4)
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image5_Doc.png', 'https://www.coursehero.com/file/55110838/SUS-Assignment-5docx/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image6_Doc.png', 'https://www.coursehero.com/file/22965867/Utilitarianism-is-the-best-approach-to-environmental-issues/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col3:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image5_QA.png', 'https://www.coursehero.com/student-questions/33217746-1-I-didnt-join-the-struggle-to-be-poor-Smuts/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col4:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image6_QA.png', 'https://www.coursehero.com/tutors-problems/Business-Other/32944358-1-INTRODUCTION-Written-for-you-by-Prof-Eccles-In/')
                st.markdown(gif_html, unsafe_allow_html=True)

    with tab2:
        tab2.markdown(f'''<h1 style='color: green; font-size:20px;'>{reco_text_1}''',unsafe_allow_html=True)
        col1,col2,col3,col4=st.columns(4)
        with st.container():
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image1_Doc.png', 'https://www.coursehero.com/file/100814111/Assignement-2docx/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image2_Doc.png', 'https://www.coursehero.com/file/74192906/SUS1501-Assignment-05pdf/')
                st.markdown(gif_html, unsafe_allow_html=True)
        tab2.write('')
        tab2.markdown(f'''<h1 style='color: blue; font-size:20px;'>{reco_text_2}''',unsafe_allow_html=True)
        with st.container():
            col1,col2,col3,col4=st.columns(4)
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image3_Doc.png', 'https://www.coursehero.com/file/67962013/JM-LUNGU-65933796docx/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image4_Doc.png', 'https://www.coursehero.com/file/33597037/SUS1501-assignment-02-S2-2018pdf/')
                st.markdown(gif_html, unsafe_allow_html=True)
        tab2.write('')
        tab2.markdown(f'''<h1 style='color: red; font-size:20px;'>{reco_text_3}''',unsafe_allow_html=True)
        with st.container():
            col1,col2,col3,col4=st.columns(4)
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image5_Doc.png', 'https://www.coursehero.com/file/55110838/SUS-Assignment-5docx/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image6_Doc.png', 'https://www.coursehero.com/file/22965867/Utilitarianism-is-the-best-approach-to-environmental-issues/')
                st.markdown(gif_html, unsafe_allow_html=True)
     
    with tab3:
        tab3.markdown(f'''<h1 style='color: green; font-size:20px;'>{reco_text_1}''',unsafe_allow_html=True)
        col1,col2,col3,col4=st.columns(4)
        with st.container():
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image1_QA.png', 'https://www.coursehero.com/tutors-problems/World-History/47646324-502-SOAPS-Eyewitness-to-Execution-5-Subject-0-Occasion-A-/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image2_QA.png', 'https://www.coursehero.com/tutors-problems/Entrepreneurship/43570754-An-analysis-of-the-inequalities-described-using-ALL-of-John/')
                st.markdown(gif_html, unsafe_allow_html=True)
        tab3.write('')
        tab3.markdown(f'''<h1 style='color: blue; font-size:20px;'>{reco_text_2}''',unsafe_allow_html=True)
        with st.container():
            col1,col2,col3,col4=st.columns(4)
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image3_QA.png', 'https://www.coursehero.com/tutors-problems/Operations-Management/40928956-Show-me-a-great-fortune-and-Ill-show-you-a-great-crime-a/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image4_QA.png', 'https://www.coursehero.com/tutors-problems/Business-Law/38537564-What-would-Kant-probably-have-said-about-van-Dijk-earning-ZAR-19/')
                st.markdown(gif_html, unsafe_allow_html=True)
        tab3.write('')
        tab3.markdown(f'''<h1 style='color: red; font-size:20px;'>{reco_text_3}''',unsafe_allow_html=True)
        with st.container():
            col1,col2,col3,col4=st.columns(4)
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image5_QA.png', 'https://www.coursehero.com/student-questions/33217746-1-I-didnt-join-the-struggle-to-be-poor-Smuts/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image6_QA.png', 'https://www.coursehero.com/tutors-problems/Business-Other/32944358-1-INTRODUCTION-Written-for-you-by-Prof-Eccles-In/')
                st.markdown(gif_html, unsafe_allow_html=True)

#essay below


if nav.split(' ')[0] == 'Essay':
    st.markdown(f'''<p style='color: black; font-size:20px;' > You have an essay due this week, try out our essay tools!  </p>''', unsafe_allow_html=True)
    # st.markdown(f'''<a style='text-align: center; color: black; font-size:28px;' href='{ai_essay_url}' > AI essay helper </a>''', unsafe_allow_html=True)
    st.page_link(ai_essay_url, label="AI essay helper", icon="🆙")
    st.page_link(paraphraser_url, label="Paraphraser", icon="🅿️")
    st.page_link(grammar_checker_url, label="Grammar checker", icon="🆓")
    tab1,tab2,tab3 = st.tabs(['All','Document','Q&A'])
    with tab1:
        tab1.markdown(f'''<h1 style='color: green; font-size:20px;'>{reco_text_1}''',unsafe_allow_html=True)
        with st.container():
            col1,col2,col3,col4=st.columns(4)
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image3_Doc.png', 'https://www.coursehero.com/file/67962013/JM-LUNGU-65933796docx/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image4_Doc.png', 'https://www.coursehero.com/file/33597037/SUS1501-assignment-02-S2-2018pdf/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col3:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image3_QA.png', 'https://www.coursehero.com/tutors-problems/Operations-Management/40928956-Show-me-a-great-fortune-and-Ill-show-you-a-great-crime-a/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col4:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image4_QA.png', 'https://www.coursehero.com/tutors-problems/Business-Law/38537564-What-would-Kant-probably-have-said-about-van-Dijk-earning-ZAR-19/')
                st.markdown(gif_html, unsafe_allow_html=True)
        tab1.write('')
        tab1.markdown(f'''<h1 style='color: blue; font-size:20px;'>{reco_text_2}''',unsafe_allow_html=True)
        with st.container():
            col1,col2,col3,col4=st.columns(4)
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image5_Doc.png', 'https://www.coursehero.com/file/55110838/SUS-Assignment-5docx/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image6_Doc.png', 'https://www.coursehero.com/file/22965867/Utilitarianism-is-the-best-approach-to-environmental-issues/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col3:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image5_QA.png', 'https://www.coursehero.com/student-questions/33217746-1-I-didnt-join-the-struggle-to-be-poor-Smuts/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col4:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image6_QA.png', 'https://www.coursehero.com/tutors-problems/Business-Other/32944358-1-INTRODUCTION-Written-for-you-by-Prof-Eccles-In/')
                st.markdown(gif_html, unsafe_allow_html=True)
        tab1.write('')
        tab1.markdown(f'''<h1 style='color: red; font-size:20px;'>{reco_text_3}''',unsafe_allow_html=True)
        with st.container():
            col1,col2,col3,col4=st.columns(4)
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image1_Doc.png', 'https://www.coursehero.com/file/100814111/Assignement-2docx/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image2_Doc.png', 'https://www.coursehero.com/file/74192906/SUS1501-Assignment-05pdf/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col3:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image1_QA.png', 'https://www.coursehero.com/tutors-problems/World-History/47646324-502-SOAPS-Eyewitness-to-Execution-5-Subject-0-Occasion-A-/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col4:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image2_QA.png', 'https://www.coursehero.com/tutors-problems/Entrepreneurship/43570754-An-analysis-of-the-inequalities-described-using-ALL-of-John/')
                st.markdown(gif_html, unsafe_allow_html=True)

    with tab2:
        tab2.markdown(f'''<h1 style='color: green; font-size:20px;'>{reco_text_1}''',unsafe_allow_html=True)
        col1,col2,col3,col4=st.columns(4)
        with st.container():
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image3_Doc.png', 'https://www.coursehero.com/file/67962013/JM-LUNGU-65933796docx/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image4_Doc.png', 'https://www.coursehero.com/file/33597037/SUS1501-assignment-02-S2-2018pdf/')
                st.markdown(gif_html, unsafe_allow_html=True)
        tab2.write('')
        tab2.markdown(f'''<h1 style='color: blue; font-size:20px;'>{reco_text_2}''',unsafe_allow_html=True)
        with st.container():
            col1,col2,col3,col4=st.columns(4)
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image5_Doc.png', 'https://www.coursehero.com/file/55110838/SUS-Assignment-5docx/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image6_Doc.png', 'https://www.coursehero.com/file/22965867/Utilitarianism-is-the-best-approach-to-environmental-issues/')
                st.markdown(gif_html, unsafe_allow_html=True)
        tab2.write('')
        tab2.markdown(f'''<h1 style='color: red; font-size:20px;'>{reco_text_3}''',unsafe_allow_html=True)
        with st.container():
            col1,col2,col3,col4=st.columns(4)
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image1_Doc.png', 'https://www.coursehero.com/file/100814111/Assignement-2docx/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image2_Doc.png', 'https://www.coursehero.com/file/74192906/SUS1501-Assignment-05pdf/')
                st.markdown(gif_html, unsafe_allow_html=True)

     
    with tab3:
        tab3.markdown(f'''<h1 style='color: green; font-size:20px;'>{reco_text_1}''',unsafe_allow_html=True)
        col1,col2,col3,col4=st.columns(4)
        with st.container():
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image3_QA.png', 'https://www.coursehero.com/tutors-problems/Operations-Management/40928956-Show-me-a-great-fortune-and-Ill-show-you-a-great-crime-a/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image4_QA.png', 'https://www.coursehero.com/tutors-problems/Business-Law/38537564-What-would-Kant-probably-have-said-about-van-Dijk-earning-ZAR-19/')
                st.markdown(gif_html, unsafe_allow_html=True)
        tab3.write('')
        tab3.markdown(f'''<h1 style='color: blue; font-size:20px;'>{reco_text_2}''',unsafe_allow_html=True)
        with st.container():
            col1,col2,col3,col4=st.columns(4)
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image5_QA.png', 'https://www.coursehero.com/student-questions/33217746-1-I-didnt-join-the-struggle-to-be-poor-Smuts/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image6_QA.png', 'https://www.coursehero.com/tutors-problems/Business-Other/32944358-1-INTRODUCTION-Written-for-you-by-Prof-Eccles-In/')
                st.markdown(gif_html, unsafe_allow_html=True)
        tab3.write('')
        tab3.markdown(f'''<h1 style='color: red; font-size:20px;'>{reco_text_3}''',unsafe_allow_html=True)
        with st.container():
            col1,col2,col3,col4=st.columns(4)
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image1_QA.png', 'https://www.coursehero.com/tutors-problems/World-History/47646324-502-SOAPS-Eyewitness-to-Execution-5-Subject-0-Occasion-A-/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image2_QA.png', 'https://www.coursehero.com/tutors-problems/Entrepreneurship/43570754-An-analysis-of-the-inequalities-described-using-ALL-of-John/')
                st.markdown(gif_html, unsafe_allow_html=True)


#Exams below
if nav.split(' ')[0] == 'Midterm' or nav.split(' ')[0] == 'Final':
    st.markdown(f'''<p style='color: black; font-size:20px;' > Your midterm/exam is coming up this week! Practice with our practice test prep tool! </p>''', unsafe_allow_html=True)
    # st.markdown(f'''<a style='text-align: center; color: black; font-size:28px;' href='{ai_essay_url}' > AI essay helper </a>''', unsafe_allow_html=True)
    st.page_link(ai_test_prep_url, label="AI test prep", icon="🆙")
    tab1,tab2,tab3 = st.tabs(['All','Document','Q&A'])
    with tab1:
        tab1.markdown(f'''<h1 style='color: green; font-size:20px;'>{reco_text_1}''',unsafe_allow_html=True)
        with st.container():
            col1,col2,col3,col4=st.columns(4)
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image7_Doc.png', 'https://www.coursehero.com/file/135628655/portfolio-template-3docx/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image8_Doc.png', 'https://www.coursehero.com/file/88996687/Assignment-05-Back-at-me-Virtue-Ethicsdoc/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col3:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image7_QA.png', 'https://www.coursehero.com/student-questions/32585086-sustainability-and-greed-assignment-5-please-help-I-am/')
                st.markdown(gif_html, unsafe_allow_html=True)
            
        tab1.write('')
        tab1.markdown(f'''<h1 style='color: blue; font-size:20px;'>{reco_text_2}''',unsafe_allow_html=True)
        with st.container():
            col1,col2,col3,col4=st.columns(4)
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image5_Doc.png', 'https://www.coursehero.com/file/55110838/SUS-Assignment-5docx/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image9_Doc.png', 'https://www.coursehero.com/file/30843691/SUS1501-Assignment-03docx/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col3:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image5_QA.png', 'https://www.coursehero.com/student-questions/33217746-1-I-didnt-join-the-struggle-to-be-poor-Smuts/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col4:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image9_QA.png', 'https://www.coursehero.com/tutors-problems/Business-Other/31915236-So-in-assignment-2-we-reflected-on-a-particular-case-involving-great/')
                st.markdown(gif_html, unsafe_allow_html=True)
        tab1.write('')
        tab1.markdown(f'''<h1 style='color: red; font-size:20px;'>{reco_text_3}''',unsafe_allow_html=True)
        with st.container():
            col1,col2,col3,col4=st.columns(4)
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image7_Doc.png', 'https://www.coursehero.com/file/135628655/portfolio-template-3docx/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image8_Doc.png', 'https://www.coursehero.com/file/88996687/Assignment-05-Back-at-me-Virtue-Ethicsdoc/')
                st.markdown(gif_html, unsafe_allow_html=True)

    with tab2:
        tab2.markdown(f'''<h1 style='color: green; font-size:20px;'>{reco_text_1}''',unsafe_allow_html=True)
        col1,col2,col3,col4=st.columns(4)
        with st.container():
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image3_Doc.png', 'https://www.coursehero.com/file/67962013/JM-LUNGU-65933796docx/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image4_Doc.png', 'https://www.coursehero.com/file/33597037/SUS1501-assignment-02-S2-2018pdf/')
                st.markdown(gif_html, unsafe_allow_html=True)
        tab2.write('')
        tab2.markdown(f'''<h1 style='color: blue; font-size:20px;'>{reco_text_2}''',unsafe_allow_html=True)
        with st.container():
            col1,col2,col3,col4=st.columns(4)
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image5_Doc.png', 'https://www.coursehero.com/file/55110838/SUS-Assignment-5docx/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image9_Doc.png', 'https://www.coursehero.com/file/30843691/SUS1501-Assignment-03docx/')
                st.markdown(gif_html, unsafe_allow_html=True)
        tab2.write('')
        tab2.markdown(f'''<h1 style='color: red; font-size:20px;'>{reco_text_3}''',unsafe_allow_html=True)
        with st.container():
            col1,col2,col3,col4=st.columns(4)
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image7_Doc.png', 'https://www.coursehero.com/file/135628655/portfolio-template-3docx/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image8_Doc.png', 'https://www.coursehero.com/file/88996687/Assignment-05-Back-at-me-Virtue-Ethicsdoc/')
                st.markdown(gif_html, unsafe_allow_html=True)

     
    with tab3:
        tab3.markdown(f'''<h1 style='color: green; font-size:20px;'>{reco_text_1}''',unsafe_allow_html=True)
        col1,col2,col3,col4=st.columns(4)
        with st.container():
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image7_QA.png', 'https://www.coursehero.com/student-questions/32585086-sustainability-and-greed-assignment-5-please-help-I-am/')
                st.markdown(gif_html, unsafe_allow_html=True)
        tab3.write('')
        tab3.markdown(f'''<h1 style='color: blue; font-size:20px;'>{reco_text_2}''',unsafe_allow_html=True)
        with st.container():
            col1,col2,col3,col4=st.columns(4)
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image5_QA.png', 'https://www.coursehero.com/student-questions/33217746-1-I-didnt-join-the-struggle-to-be-poor-Smuts/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image9_QA.png', 'https://www.coursehero.com/tutors-problems/Business-Other/31915236-So-in-assignment-2-we-reflected-on-a-particular-case-involving-great/')
                st.markdown(gif_html, unsafe_allow_html=True)
        tab3.write('')
        tab3.markdown(f'''<h1 style='color: red; font-size:20px;'>{reco_text_3}''',unsafe_allow_html=True)
        with st.container():
            col1,col2,col3,col4=st.columns(4)
            with col1:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image5_QA.png', 'https://www.coursehero.com/student-questions/33217746-1-I-didnt-join-the-struggle-to-be-poor-Smuts/')
                st.markdown(gif_html, unsafe_allow_html=True)
            with col2:
                gif_html = get_img_with_href('./analytics/wn_analysis_details/streamlit_demo/Assets/SUS1501_image9_QA.png', 'https://www.coursehero.com/tutors-problems/Business-Other/31915236-So-in-assignment-2-we-reflected-on-a-particular-case-involving-great/')
                st.markdown(gif_html, unsafe_allow_html=True)

