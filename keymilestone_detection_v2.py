import streamlit as st
from streamlit_pills import pills
import base64
import os
import plotly.express as px
import pandas as pd
from streamlit_modal import Modal
import streamlit.components.v1 as components
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

def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    components.html(open_script)

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

practice_test_text_header = 'Our practice tests are generated from the specific course materials relevant to your milestone'
pt_text_1 = 'Pre test: Test your knowledge on required concepts'
pt_text_2 = 'Post test: Re-enforce concepts that are you week at'
pt_text_3 = 'Exam style practice tests'


flashcard_text_header = 'Checkout flashcards generates specifically for your milestone.'
fc_text_1 = 'Flashcards covering all concepts'
fc_text_2 = 'Re-enforcing weak concepts'
fc_text_3 = ''

study_guide_text_header = 'Study guides to help you prepare for your milestone.'

#end of side bar configuration
text_to_render = f'''<h1 style='color: blue; font-size:28px;'> Start preparing for your {nav.split(' ')[0]} that is happening on the week of {nav.split(' ')[-1]}  </h1>'''
st.markdown(text_to_render, unsafe_allow_html=True)

topics1 = ['All','Historical Perspectives on Greed and Environmental Exploitation', 'Economic Theories and Sustainability', 'The Role of Corporations in Environmental Degradation']
topics2 = ['All','Consumerism and Its Impact on Sustainability', 'Ethical Consumerism and Sustainable Living', 'Government Policies, Regulations, and Sustainability']
topics3 = ['All','International Agreements on Climate Changes and Their Impact', 'Renewable Energy Sources and Sustainability', 'Fossil Fuels, Greed, and Environmental Policies']
topics4 = ['All','Water Scarcity, Privatization, and Sustainability', 'Deforestation and Biodiversity Loss', 'Sustainable Agriculture vs. Industrial Farming']
topics5 = ['All','Sustainable Agricultures vs Industrial Farming', 'The Impact of Fishing and Aquaculture on Marine Ecosystems', 'Waste Management and Recycling Practices']

date_topic_mapping = {
    '2024-06-03': topics1,
    '2024-06-10': topics2,
    '2024-06-17': topics3,
    '2024-07-08': topics4,
    '2024-08-19': topics5
}

topic_text = 'Topics covered in this milestone.'

doc_assets = {
    1:('streamlit_demo1/Assets/SUS1501_image1_Doc.png','https://www.coursehero.com/file/100814111/Assignement-2docx/'),
    2:('streamlit_demo1/Assets/SUS1501_image2_Doc.png','https://www.coursehero.com/file/74192906/SUS1501-Assignment-05pdf/'),
    3:('streamlit_demo1/Assets/SUS1501_image3_Doc.png','https://www.coursehero.com/file/67962013/JM-LUNGU-65933796docx/'),
    4:('streamlit_demo1/Assets/SUS1501_image4_Doc.png','https://www.coursehero.com/file/33597037/SUS1501-assignment-02-S2-2018pdf/'),
    5:('streamlit_demo1/Assets/SUS1501_image5_Doc.png','https://www.coursehero.com/file/55110838/SUS-Assignment-5docx/'),
    6:('streamlit_demo1/Assets/SUS1501_image6_Doc.png','https://www.coursehero.com/file/22965867/Utilitarianism-is-the-best-approach-to-environmental-issues/'),
    7:('streamlit_demo1/Assets/SUS1501_image7_Doc.png','https://www.coursehero.com/file/135628655/portfolio-template-3docx/'),
    8:('streamlit_demo1/Assets/SUS1501_image8_Doc.png','https://www.coursehero.com/file/88996687/Assignment-05-Back-at-me-Virtue-Ethicsdoc/'),
    9:('streamlit_demo1/Assets/SUS1501_image9_Doc.png','https://www.coursehero.com/file/30843691/SUS1501-Assignment-03docx/'),
}

qa_assets = {
    1:('streamlit_demo1/Assets/SUS1501_image1_QA.png','https://www.coursehero.com/tutors-problems/World-History/47646324-502-SOAPS-Eyewitness-to-Execution-5-Subject-0-Occasion-A-/'),
    2:('streamlit_demo1/Assets/SUS1501_image2_QA.png','https://www.coursehero.com/tutors-problems/Entrepreneurship/43570754-An-analysis-of-the-inequalities-described-using-ALL-of-John/'),
    3:('streamlit_demo1/Assets/SUS1501_image3_QA.png','https://www.coursehero.com/tutors-problems/Operations-Management/40928956-Show-me-a-great-fortune-and-Ill-show-you-a-great-crime-a/'),
    4:('streamlit_demo1/Assets/SUS1501_image4_QA.png','https://www.coursehero.com/tutors-problems/Business-Law/38537564-What-would-Kant-probably-have-said-about-van-Dijk-earning-ZAR-19/'),
    5:('streamlit_demo1/Assets/SUS1501_image5_QA.png','https://www.coursehero.com/student-questions/33217746-1-I-didnt-join-the-struggle-to-be-poor-Smuts/'),
    6:('streamlit_demo1/Assets/SUS1501_image6_QA.png','https://www.coursehero.com/file/22965867/Utilitarianism-is-the-best-approach-to-environmental-issues/'),
    7:('streamlit_demo1/Assets/SUS1501_image7_QA.png','https://www.coursehero.com/student-questions/32585086-sustainability-and-greed-assignment-5-please-help-I-am/'),
    8:('streamlit_demo1/Assets/SUS1501_image8_QA.png','https://www.coursehero.com/student-questions/32313861-Is-it-good-for-other-to-earn-R1-9-billion-while-other/'),
    9:('streamlit_demo1/Assets/SUS1501_image9_QA.png','https://www.coursehero.com/tutors-problems/Business-Other/31915236-So-in-assignment-2-we-reflected-on-a-particular-case-involving-great/'),
}

asset_to_topic_map = {
    1:[1,3],
    2:[2,3],
    3:[1,2],
    4:[1,3],
    5:[2,3],
    6:[1,2],
    7:[1,3],
    8:[2,3],
    9:[1,2],
}
fc_asset_to_topic_map = {
    1:[1,3],
    2:[2,3],
    3:[1,2],
    4:[1,3],
    5:[2,3],
    6:[1,2],
    7:[1,3],
}


practice_test_link='https://www.coursehero.com/quiz/course/5182587?numberOfQuestions=10topics[]=The%20Role%20of%20Corporations%20in%20Sustainability&topics[]=Ethical%20Consumption%20and%20Sustainable%20Living&topics[]=Case%20Studies:%20The%20Impact%20of%20Greed%20on%20Sustainability&topics[]=The%20Psychology%20of%20Greed%20and%20Its%20Environmental%20Impacts&topics[]=The%20Future%20of%20Sustainability:%20Trends%20and%20Predictions&topics[]=The%20Economics%20of%20Greed%20and%20Environmental%20Degradation&topics[]=Sustainable%20Development%20Goals%20(SDGs)%20and%20Global%20Initiatives&topics[]=Sustainability%20in%20Developing%20vs.%20Developed%20Countries&topics[]=Sustainability%20as%20a%20Business%20Model&topics[]=Promoting%20Behavioral%20Change%20for%20Sustainability&topics[]=Preparing%20for%20a%20Sustainable%20Career&topics[]=Policy%20and%20Legislation%20for%20Environmental%20Protection&topics[]=International%20Agreements%20on%20Climate%20Change&topics[]=Innovative%20Solutions%20to%20Combat%20Greed-Driven%20Environmental%20Harm&topics[]=Green%20Technologies%20and%20Renewable%20Energy&topics[]=Engaging%20Stakeholders%20in%20Sustainability%20Efforts&topics[]=Economic%20Inequalities%20and%20Environmental%20Justice&topics[]=Consumerism%20and%20Its%20Effects%20on%20the%20Environment&topics[]=Community-based%20Sustainability%20Projects&topics[]=Barriers%20to%20Sustainable%20Innovation&topics[]=Historical%20Perspectives%20on%20Environmental%20Exploitation'
if nav.split(' ')[0] == 'Assignment':
    selected = pills(topic_text, date_topic_mapping[nav.split(' ')[-1]],clearable = False)
    indx_of_selected = date_topic_mapping[nav.split(' ')[-1]].index(selected)
    tab4,tab5,tab6,tab1,tab2,tab3 = st.tabs(['Practice Problems','Flashcards','Study Guides','All Contents','Document','Q&A'])
    with tab1:
        st.markdown(f'''<h1 style='color: green; font-size:20px;'>{reco_text_1} </h1>''',unsafe_allow_html=True)
        doc_factor=1
        qa_factor=-1
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+doc_factor]+[0]:
                        gif_html = get_img_with_href(doc_assets[indx+doc_factor][0], doc_assets[indx+doc_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
                else:
                    if indx_of_selected in asset_to_topic_map[indx+qa_factor]+[0]:
                        gif_html = get_img_with_href(qa_assets[indx+qa_factor][0], qa_assets[indx+qa_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
        st.write('')
        st.markdown(f'''<h1 style='color: blue; font-size:20px;'>{reco_text_2}''',unsafe_allow_html=True)
        doc_factor=3
        qa_factor=1
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+doc_factor]+[0]:
                        gif_html = get_img_with_href(doc_assets[indx+doc_factor][0], doc_assets[indx+doc_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
                else:
                    if indx_of_selected in asset_to_topic_map[indx+qa_factor]+[0]:
                        gif_html = get_img_with_href(qa_assets[indx+qa_factor][0], qa_assets[indx+qa_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
        st.write('')
        st.markdown(f'''<h1 style='color: red; font-size:20px;'>{reco_text_3}''',unsafe_allow_html=True)
        doc_factor=5
        qa_factor=3
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+doc_factor]+[0]:
                        gif_html = get_img_with_href(doc_assets[indx+doc_factor][0], doc_assets[indx+doc_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
                else:
                    if indx_of_selected in asset_to_topic_map[indx+qa_factor]+[0]:
                        gif_html = get_img_with_href(qa_assets[indx+qa_factor][0], qa_assets[indx+qa_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)

    with tab2:
        st.markdown(f'''<h1 style='color: green; font-size:20px;'>{reco_text_1}''',unsafe_allow_html=True)
        doc_factor=1
        qa_factor=-1
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+doc_factor]+[0]:
                        gif_html = get_img_with_href(doc_assets[indx+doc_factor][0], doc_assets[indx+doc_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
        st.write('')
        st.markdown(f'''<h1 style='color: blue; font-size:20px;'>{reco_text_2}''',unsafe_allow_html=True)
        doc_factor=3
        qa_factor=1
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+doc_factor]+[0]:
                        gif_html = get_img_with_href(doc_assets[indx+doc_factor][0], doc_assets[indx+doc_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
        st.write('')
        st.markdown(f'''<h1 style='color: red; font-size:20px;'>{reco_text_3}''',unsafe_allow_html=True)
        doc_factor=5
        qa_factor=3
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+doc_factor]+[0]:
                        gif_html = get_img_with_href(doc_assets[indx+doc_factor][0], doc_assets[indx+doc_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
     
    with tab3:
        st.markdown(f'''<h1 style='color: green; font-size:20px;'>{reco_text_1}''',unsafe_allow_html=True)
        doc_factor=1
        qa_factor=doc_factor
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+qa_factor]+[0]:
                        gif_html = get_img_with_href(qa_assets[indx+qa_factor][0], qa_assets[indx+qa_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
        st.write('')
        st.markdown(f'''<h1 style='color: blue; font-size:20px;'>{reco_text_2}''',unsafe_allow_html=True)
        doc_factor=3
        qa_factor=doc_factor
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+qa_factor]+[0]:
                        gif_html = get_img_with_href(qa_assets[indx+qa_factor][0], qa_assets[indx+qa_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
        st.write('')
        st.markdown(f'''<h1 style='color: red; font-size:20px;'>{reco_text_3}''',unsafe_allow_html=True)
        doc_factor=5
        qa_factor=doc_factor
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+qa_factor]+[0]:
                        gif_html = get_img_with_href(qa_assets[indx+qa_factor][0], qa_assets[indx+qa_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
    with tab6:
        gif_html = get_img_with_href('streamlit_demo1/Assets/study_guide_assets/SG_1.jpg','https://www.coursehero.com/dashboard/')
        st.markdown(gif_html, unsafe_allow_html=True)
    with tab5:
        @st.experimental_dialog("Create your own flashcards")
        def generate_fc():
            with st.container():
                st.write("Create your own flashcard specific to the topics and courses you are taking!")
                st.markdown(''':green[Select topics you want to cover in the flashcards below]''')
                for res in date_topic_mapping[nav.split(' ')[-1]][1:]:
                    values = st.checkbox(res)
                st.session_state.generate = {'generated'}
                if st.button('Generate'):
                    st.write("Flashcards generated successfully")
                    open_page(ai_test_prep_url)
                    

        if st.button('Generate a topic specific flashcards!'):
            generate_fc()

        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx_of_selected in asset_to_topic_map[indx+1]+[0]:
                    gif_html = get_img_with_href(f'streamlit_demo1/Assets/flashcard_assets/FC{indx+1}.jpg',ai_test_prep_url)
                    cols.markdown(gif_html, unsafe_allow_html=True)
            for indx,cols in enumerate(st.columns(4)):
                if indx>=3:
                    gif_html = get_img_with_href('streamlit_demo1/Assets/flashcard_assets/FC_own.jpg',ai_test_prep_url)
                    cols.markdown(gif_html, unsafe_allow_html=True)
                    break
                if indx_of_selected in asset_to_topic_map[indx+4]+[0]:
                    gif_html = get_img_with_href(f'streamlit_demo1/Assets/flashcard_assets/FC{indx+4}_C.jpg',ai_test_prep_url)
                    cols.markdown(gif_html, unsafe_allow_html=True)
            d = {'Total':[7],'Completed':[3]}
            df=pd.DataFrame(d)
            df['Remaining'] = df['Total']-df['Completed']
            df['Progress'] = ((df['Completed']/df['Total'])*100).round(1)
            display_text = f"Completed: {df['Progress'][0]}%"
            fig = px.bar(df,y='Total',x=['Completed','Remaining'],title='Flashcard Progress',orientation='h',barmode='stack',text=[display_text],
                    color_discrete_map={'Completed':'green', 'Remaining':'whitesmoke'},width = 1000, height = 300)
            fig.update_layout(showlegend=False,xaxis_title='Total Flashcards available')
            fig.for_each_trace(lambda t: t.update(text = []) if t.name not in ['Remaining'] else ())
            st.write(fig)

    with tab4:
        # if 'content_state' not in st.session.state:
        #     st.session_state.content_state = 0
        # if 'topic_state' not in st.session.state:
        #     st.session_state.topic_state = 0
        @st.experimental_dialog("Create a custom practice test",width='large')
        def generate_pt():
            with st.container():
                st.write("Create a custom practice test from either topics or recommended document/questions!")
                selected_method = st.radio('Choose how to generate your practict tests', ['By Content','By Topics'],horizontal=True,index=None)
                if selected_method == 'By Content':
                    concept_list = []
                    st.markdown(''':blue[Select from documents or QA below you want to cover in the practice test below]''')
                    for res in doc_assets.keys():
                        if res<=4:
                            values = st.checkbox('document_'+str(res)+' document_title')
                        else:
                            values = st.checkbox('question_'+str(res)+' question_title')
                        if values:
                            concept_list.extend(fc_asset_to_topic_map[res])
                            concept_list = list(set(concept_list))
                    st.markdown(''':green[Topics covered with selected documents & questions]''')
                    for c in range(len(date_topic_mapping[nav.split(' ')[-1]])):
                        if c in concept_list:
                            st.markdown(f'''* {date_topic_mapping[nav.split(' ')[-1]][c]}''')
                    if st.button('Generate'):
                            st.write("Practice test generated successfully")
                            open_page(ai_test_prep_url)
                if selected_method == 'By Topics':
                    for res2 in date_topic_mapping[nav.split(' ')[-1]][1:]:
                        values2 = st.checkbox(res2)
                    if st.button('Generate'):
                            st.write("Practice test generated successfully")
                            open_page(ai_test_prep_url)    
        if st.button('Generate a custom practict test today'):
            generate_pt()

        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx_of_selected in asset_to_topic_map[indx+1]+[0]:
                    gif_html = get_img_with_href(f'streamlit_demo1/Assets/practice_problem_assets/PT{indx+1}.jpg',ai_test_prep_url)
                    cols.markdown(gif_html, unsafe_allow_html=True)
            for indx,cols in enumerate(st.columns(4)):
                if indx>=3:
                    # gif_html = get_img_with_href('streamlit_demo1/Assets/flashcard_assets/FC_own.jpg',ai_test_prep_url)
                    # cols.markdown(gif_html, unsafe_allow_html=True)
                    break
                if indx_of_selected in asset_to_topic_map[indx+4]+[0]:
                    gif_html = get_img_with_href(f'streamlit_demo1/Assets/practice_problem_assets/PT{indx+4}_C.jpg',ai_test_prep_url)
                    cols.markdown(gif_html, unsafe_allow_html=True)
        tc1,tc2 = st.columns([1,3])
        # overall score 
        with tc1:
            d2 = {'score':[70],'text_score':'70%'}
            df = pd.DataFrame(d2)
            fig = px.bar(df,y='score',title='Overall score',text='text_score',width = 300, height = 500)
            fig.update_layout(showlegend=False,xaxis_title='Practice test score',yaxis_range=[0,100])
            st.write(fig)
        with tc2:
            d3={'topics':date_topic_mapping[nav.split(' ')[-1]][1:],
                'score':[100,60,75],
                'text_score':['100%','60%','75%'],
                }
            df = pd.DataFrame(d3)
            df.sort_values('score',ascending=False,inplace=True)
            fig = px.bar(df,y='topics',x='score',title='Topic score',text='text_score',color='topics',width = 1000, height = 500,orientation='h')
            fig.update_layout(showlegend=False,xaxis_title='Practice test score by topics',xaxis_range=[0,100])
            st.write(fig)

        d = {'Total':[7],'Completed':[3]}
        df=pd.DataFrame(d)
        df['Remaining'] = df['Total']-df['Completed']
        df['Progress'] = ((df['Completed']/df['Total'])*100).round(1)
        display_text = f"Completed: {df['Progress'][0]}%"
        fig = px.bar(df,y='Total',x=['Completed','Remaining'],title='Practice Test Progress',orientation='h',barmode='stack',text=[display_text],
                color_discrete_map={'Completed':'green', 'Remaining':'whitesmoke'},width = 1000, height = 300)
        fig.update_layout(showlegend=False,xaxis_title='Total Practice test available')
        fig.for_each_trace(lambda t: t.update(text = []) if t.name not in ['Remaining'] else ())
        st.write(fig)
#essay below
if nav.split(' ')[0] == 'Essay':
    st.markdown(f'''<p style='color: black; font-size:20px;' > You have an essay due this week, try out our essay tools!  </p>''', unsafe_allow_html=True)
    # st.markdown(f'''<a style='text-align: center; color: black; font-size:28px;' href='{ai_essay_url}' > AI essay helper </a>''', unsafe_allow_html=True)
    c1,c2,c3=st.columns(3)
    c1.page_link(ai_essay_url, label="AI essay helper", icon="🆙")
    c2.page_link(paraphraser_url, label="Paraphraser", icon="🅿️")
    c3.page_link(grammar_checker_url, label="Grammar checker", icon="🆓")
    selected = pills(topic_text, date_topic_mapping[nav.split(' ')[-1]],clearable = False)
    indx_of_selected = date_topic_mapping[nav.split(' ')[-1]].index(selected)
    tab4,tab5,tab6,tab1,tab2,tab3 = st.tabs(['Practice Problems','Flashcards','Study Guides','All Contents','Document','Q&A'])
    # 3,1
    # 5,3
    # 7,5
    with tab1:
        st.markdown(f'''<h1 style='color: green; font-size:20px;'>{reco_text_1} </h1>''',unsafe_allow_html=True)
        doc_factor=3
        qa_factor=1
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+doc_factor]+[0]:
                        gif_html = get_img_with_href(doc_assets[indx+doc_factor][0], doc_assets[indx+doc_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
                else:
                    if indx_of_selected in asset_to_topic_map[indx+qa_factor]+[0]:
                        gif_html = get_img_with_href(qa_assets[indx+qa_factor][0], qa_assets[indx+qa_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
        st.write('')
        st.markdown(f'''<h1 style='color: blue; font-size:20px;'>{reco_text_2}''',unsafe_allow_html=True)
        doc_factor=5
        qa_factor=3
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+doc_factor]+[0]:
                        gif_html = get_img_with_href(doc_assets[indx+doc_factor][0], doc_assets[indx+doc_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
                else:
                    if indx_of_selected in asset_to_topic_map[indx+qa_factor]+[0]:
                        gif_html = get_img_with_href(qa_assets[indx+qa_factor][0], qa_assets[indx+qa_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
        st.write('')
        st.markdown(f'''<h1 style='color: red; font-size:20px;'>{reco_text_3}''',unsafe_allow_html=True)
        doc_factor=7
        qa_factor=5
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+doc_factor]+[0]:
                        gif_html = get_img_with_href(doc_assets[indx+doc_factor][0], doc_assets[indx+doc_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
                else:
                    if indx_of_selected in asset_to_topic_map[indx+qa_factor]+[0]:
                        gif_html = get_img_with_href(qa_assets[indx+qa_factor][0], qa_assets[indx+qa_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)

    with tab2:
        st.markdown(f'''<h1 style='color: green; font-size:20px;'>{reco_text_1}''',unsafe_allow_html=True)
        doc_factor=3
        qa_factor=1
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+doc_factor]+[0]:
                        gif_html = get_img_with_href(doc_assets[indx+doc_factor][0], doc_assets[indx+doc_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
        st.write('')
        st.markdown(f'''<h1 style='color: blue; font-size:20px;'>{reco_text_2}''',unsafe_allow_html=True)
        doc_factor=5
        qa_factor=3
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+doc_factor]+[0]:
                        gif_html = get_img_with_href(doc_assets[indx+doc_factor][0], doc_assets[indx+doc_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
        st.write('')
        st.markdown(f'''<h1 style='color: red; font-size:20px;'>{reco_text_3}''',unsafe_allow_html=True)
        doc_factor=7
        qa_factor=5
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+doc_factor]+[0]:
                        gif_html = get_img_with_href(doc_assets[indx+doc_factor][0], doc_assets[indx+doc_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
     
    with tab3:
        st.markdown(f'''<h1 style='color: green; font-size:20px;'>{reco_text_1}''',unsafe_allow_html=True)
        doc_factor=3
        qa_factor=doc_factor
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+qa_factor]+[0]:
                        gif_html = get_img_with_href(qa_assets[indx+qa_factor][0], qa_assets[indx+qa_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
        st.write('')
        st.markdown(f'''<h1 style='color: blue; font-size:20px;'>{reco_text_2}''',unsafe_allow_html=True)
        doc_factor=5
        qa_factor=doc_factor
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+qa_factor]+[0]:
                        gif_html = get_img_with_href(qa_assets[indx+qa_factor][0], qa_assets[indx+qa_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
        st.write('')
        st.markdown(f'''<h1 style='color: red; font-size:20px;'>{reco_text_3}''',unsafe_allow_html=True)
        doc_factor=7
        qa_factor=doc_factor
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+qa_factor]+[0]:
                        gif_html = get_img_with_href(qa_assets[indx+qa_factor][0], qa_assets[indx+qa_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
    with tab6:
        gif_html = get_img_with_href('streamlit_demo1/Assets/study_guide_assets/SG_1.jpg','https://www.coursehero.com/dashboard/')
        st.markdown(gif_html, unsafe_allow_html=True)
    with tab5:
        @st.experimental_dialog("Create your own flashcards")
        def generate_fc():
            with st.container():
                st.write("Create your own flashcard specific to the topics and courses you are taking!")
                st.markdown(''':green[Select topics you want to cover in the flashcards below]''')
                for res in date_topic_mapping[nav.split(' ')[-1]][1:]:
                    values = st.checkbox(res)
                st.session_state.generate = {'generated'}
                if st.button('Generate'):
                    st.write("Flashcards generated successfully")
                    open_page(ai_test_prep_url)
                    

        if st.button('Generate a topic specific flashcards!'):
            generate_fc()
                
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx_of_selected in asset_to_topic_map[indx+3]+[0]:
                    gif_html = get_img_with_href(f'streamlit_demo1/Assets/flashcard_assets/FC{indx+3}.jpg',ai_test_prep_url)
                    cols.markdown(gif_html, unsafe_allow_html=True)
            
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+1]+[0]:
                        gif_html = get_img_with_href(f'streamlit_demo1/Assets/flashcard_assets/FC{indx+1}.jpg',ai_test_prep_url)
                        cols.markdown(gif_html, unsafe_allow_html=True)
                if indx>=2:
                    # gif_html = get_img_with_href('streamlit_demo1/Assets/flashcard_assets/FC_own.jpg',ai_test_prep_url)
                    # cols.markdown(gif_html, unsafe_allow_html=True)
                    # st.markdown("""
                    #         <style>.element-container:has(#button-after) + div button {
                    #         /* APPLY YOUR STYLING HERE */
                    #         }</style>""", unsafe_allow_html=True)
                    break
                    
        d = {'Total':[6],'Completed':[0]}
        df=pd.DataFrame(d)
        df['Remaining'] = df['Total']-df['Completed']
        df['Progress'] = ((df['Completed']/df['Total'])*100).round(1)
        display_text = f"Completed: {df['Progress'][0]}%"
        fig = px.bar(df,y='Total',x=['Completed','Remaining'],title='Flashcard Progress',orientation='h',barmode='stack',text=[display_text],
                color_discrete_map={'Completed':'green', 'Remaining':'whitesmoke'},width = 1000, height = 300)
        fig.update_layout(showlegend=False,xaxis_title='Total Flashcards available')
        fig.for_each_trace(lambda t: t.update(text = []) if t.name not in ['Remaining'] else ())
        st.write(fig)

    with tab4:
        @st.experimental_dialog("Create a custom practice test",width='large')
        def generate_pt():
            with st.container():
                st.write("Create a custom practice test from either topics or recommended document/questions!")
                selected_method = st.radio('Choose how to generate your practict tests', ['By Content','By Topics'],horizontal=True,index=None)
                if selected_method == 'By Content':
                    concept_list = []
                    st.markdown(''':blue[Select from documents or QA below you want to cover in the practice test below]''')
                    for res in doc_assets.keys():
                        if res<=4:
                            values = st.checkbox('document_'+str(res)+' document_title')
                        else:
                            values = st.checkbox('question_'+str(res)+' question_title')
                        if values:
                            concept_list.extend(fc_asset_to_topic_map[res])
                            concept_list = list(set(concept_list))
                    st.markdown(''':green[Topics covered with selected documents & questions]''')
                    for c in range(len(date_topic_mapping[nav.split(' ')[-1]])):
                        if c in concept_list:
                            st.markdown(f'''* {date_topic_mapping[nav.split(' ')[-1]][c]}''')
                    if st.button('Generate'):
                            st.write("Practice test generated successfully")
                            open_page(ai_test_prep_url)
                if selected_method == 'By Topics':
                    for res2 in date_topic_mapping[nav.split(' ')[-1]][1:]:
                        values2 = st.checkbox(res2)
                    if st.button('Generate'):
                            st.write("Practice test generated successfully")
                            open_page(ai_test_prep_url)    
        if st.button('Generate a custom practict test today'):
            generate_pt()

        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx_of_selected in asset_to_topic_map[indx+3]+[0]:
                    gif_html = get_img_with_href(f'streamlit_demo1/Assets/practice_problem_assets/PT{indx+3}.jpg',ai_test_prep_url)
                    cols.markdown(gif_html, unsafe_allow_html=True)
            
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+1]+[0]:
                        gif_html = get_img_with_href(f'streamlit_demo1/Assets/practice_problem_assets/PT{indx+1}.jpg',ai_test_prep_url)
                        cols.markdown(gif_html, unsafe_allow_html=True)
                if indx>=2:
                    break
        tc1,tc2 = st.columns([1,3])
        # overall score 
        with tc1:
            d2 = {'score':[0],'text_score':'0%'}
            df = pd.DataFrame(d2)
            fig = px.bar(df,y='score',title='Overall score',text='text_score',width = 300, height = 500,)
            fig.update_layout(showlegend=False,xaxis_title='Practice test score',yaxis_range=[0,100])
            st.write(fig)
        with tc2:
            d3={'topics':date_topic_mapping[nav.split(' ')[-1]][1:],
                'score':[0,0,0],
                'text_score':['0%','0%','0%'],
                }
            df = pd.DataFrame(d3)
            df.sort_values('score',ascending=False,inplace=True)
            fig = px.bar(df,y='topics',x='score',title='Topic score',text='text_score',color='topics',width = 1000, height = 500,orientation='h')
            fig.update_layout(showlegend=False,xaxis_title='Practice test score by topics',xaxis_range=[0,100])
            st.write(fig)

        d = {'Total':[6],'Completed':[0]}
        df=pd.DataFrame(d)
        df['Remaining'] = df['Total']-df['Completed']
        df['Progress'] = ((df['Completed']/df['Total'])*100).round(1)
        display_text = f"Completed: {df['Progress'][0]}%"
        fig = px.bar(df,y='Total',x=['Completed','Remaining'],title='Practice Test Progress',orientation='h',barmode='stack',text=[display_text],
                color_discrete_map={'Completed':'green', 'Remaining':'whitesmoke'},width = 1000, height = 300)
        fig.update_layout(showlegend=False,xaxis_title='Total Practice test available')
        fig.for_each_trace(lambda t: t.update(text = []) if t.name not in ['Remaining'] else ())
        st.write(fig)
#Exams below
if nav.split(' ')[0] == 'Midterm' or nav.split(' ')[0] == 'Final':
    st.markdown(f'''<p style='color: black; font-size:20px;' > Your midterm/exam is coming up this week! Practice with our practice test prep tool! </p>''', unsafe_allow_html=True)
    # st.markdown(f'''<a style='text-align: center; color: black; font-size:28px;' href='{ai_essay_url}' > AI essay helper </a>''', unsafe_allow_html=True)
    st.page_link(ai_test_prep_url, label="AI test prep", icon="🆙")
    selected = pills(topic_text, date_topic_mapping[nav.split(' ')[-1]],clearable = False)
    indx_of_selected = date_topic_mapping[nav.split(' ')[-1]].index(selected)
    tab4,tab5,tab6,tab1,tab2,tab3 = st.tabs(['Practice Problems','Flashcards','Study Guides','All Contents','Document','Q&A'])
    # 8,6
    # 6,4
    # 5,3
    with tab1:
        st.markdown(f'''<h1 style='color: green; font-size:20px;'>{reco_text_1} </h1>''',unsafe_allow_html=True)
        doc_factor=8
        qa_factor=6
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+doc_factor]+[0]:
                        gif_html = get_img_with_href(doc_assets[indx+doc_factor][0], doc_assets[indx+doc_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
                else:
                    if indx_of_selected in asset_to_topic_map[indx+qa_factor]+[0]:
                        gif_html = get_img_with_href(qa_assets[indx+qa_factor][0], qa_assets[indx+qa_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
        st.write('')
        st.markdown(f'''<h1 style='color: blue; font-size:20px;'>{reco_text_2}''',unsafe_allow_html=True)
        doc_factor=6
        qa_factor=4
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+doc_factor]+[0]:
                        gif_html = get_img_with_href(doc_assets[indx+doc_factor][0], doc_assets[indx+doc_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
                else:
                    if indx_of_selected in asset_to_topic_map[indx+qa_factor]+[0]:
                        gif_html = get_img_with_href(qa_assets[indx+qa_factor][0], qa_assets[indx+qa_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
        st.write('')
        st.markdown(f'''<h1 style='color: red; font-size:20px;'>{reco_text_3}''',unsafe_allow_html=True)
        doc_factor=5
        qa_factor=3
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+doc_factor]+[0]:
                        gif_html = get_img_with_href(doc_assets[indx+doc_factor][0], doc_assets[indx+doc_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
                else:
                    if indx_of_selected in asset_to_topic_map[indx+qa_factor]+[0]:
                        gif_html = get_img_with_href(qa_assets[indx+qa_factor][0], qa_assets[indx+qa_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)

    with tab2:
        st.markdown(f'''<h1 style='color: green; font-size:20px;'>{reco_text_1}''',unsafe_allow_html=True)
        doc_factor=8
        qa_factor=6
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+doc_factor]+[0]:
                        gif_html = get_img_with_href(doc_assets[indx+doc_factor][0], doc_assets[indx+doc_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
        st.write('')
        st.markdown(f'''<h1 style='color: blue; font-size:20px;'>{reco_text_2}''',unsafe_allow_html=True)
        doc_factor=6
        qa_factor=4
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+doc_factor]+[0]:
                        gif_html = get_img_with_href(doc_assets[indx+doc_factor][0], doc_assets[indx+doc_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
        st.write('')
        st.markdown(f'''<h1 style='color: red; font-size:20px;'>{reco_text_3}''',unsafe_allow_html=True)
        doc_factor=5
        qa_factor=3
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+doc_factor]+[0]:
                        gif_html = get_img_with_href(doc_assets[indx+doc_factor][0], doc_assets[indx+doc_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
     
    with tab3:
        tab3.markdown(f'''<h1 style='color: green; font-size:20px;'>{reco_text_1}''',unsafe_allow_html=True)
        doc_factor=8
        qa_factor=doc_factor
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+qa_factor]+[0]:
                        gif_html = get_img_with_href(qa_assets[indx+qa_factor][0], qa_assets[indx+qa_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
        st.write('')
        st.markdown(f'''<h1 style='color: blue; font-size:20px;'>{reco_text_2}''',unsafe_allow_html=True)
        doc_factor=6
        qa_factor=doc_factor
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+qa_factor]+[0]:
                        gif_html = get_img_with_href(qa_assets[indx+qa_factor][0], qa_assets[indx+qa_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
        st.write('')
        st.markdown(f'''<h1 style='color: red; font-size:20px;'>{reco_text_3}''',unsafe_allow_html=True)
        doc_factor=5
        qa_factor=doc_factor
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=1:
                    if indx_of_selected in asset_to_topic_map[indx+qa_factor]+[0]:
                        gif_html = get_img_with_href(qa_assets[indx+qa_factor][0], qa_assets[indx+qa_factor][1])
                        cols.markdown(gif_html, unsafe_allow_html=True)
    with tab6:
        gif_html = get_img_with_href('streamlit_demo1/Assets/study_guide_assets/SG_1.jpg','https://www.coursehero.com/dashboard/')
        st.markdown(gif_html, unsafe_allow_html=True)
    with tab5:
        @st.experimental_dialog("Create your own flashcards")
        def generate_fc():
            with st.container():
                st.write("Create your own flashcard specific to the topics and courses you are taking!")
                st.markdown(''':green[Select topics you want to cover in the flashcards below]''')
                for res in date_topic_mapping[nav.split(' ')[-1]][1:]:
                    values = st.checkbox(res)
                st.session_state.generate = {'generated'}
                if st.button('Generate'):
                    st.write("Flashcards generated successfully")
                    open_page(ai_test_prep_url)

        if st.button('Generate a topic specific flashcards!'):
            generate_fc()
        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=3:
                    if indx_of_selected in asset_to_topic_map[indx+1]+[0]:
                        gif_html = get_img_with_href(f'streamlit_demo1/Assets/flashcard_assets/FC{indx+1}.jpg',ai_test_prep_url)
                        cols.markdown(gif_html, unsafe_allow_html=True)
                else:
                    if indx_of_selected in asset_to_topic_map[indx+1]+[0]:
                        gif_html = get_img_with_href(f'streamlit_demo1/Assets/flashcard_assets/FC{indx+1}_C.jpg',ai_test_prep_url)
                        cols.markdown(gif_html, unsafe_allow_html=True)
            for indx,cols in enumerate(st.columns(4)):
                if indx>=2:
                    # gif_html = get_img_with_href('streamlit_demo1/Assets/flashcard_assets/FC_own.jpg',ai_test_prep_url)
                    # cols.markdown(gif_html, unsafe_allow_html=True)
                    break
                if indx_of_selected in asset_to_topic_map[indx+5]+[0]:
                    gif_html = get_img_with_href(f'streamlit_demo1/Assets/flashcard_assets/FC{indx+5}_C.jpg',ai_test_prep_url)
                    cols.markdown(gif_html, unsafe_allow_html=True)
            d = {'Total':[6],'Completed':[2]}
            df=pd.DataFrame(d)
            df['Remaining'] = df['Total']-df['Completed']
            df['Progress'] = ((df['Completed']/df['Total'])*100).round(1)
            display_text = f"Completed: {df['Progress'][0]}%"
            fig = px.bar(df,y='Total',x=['Completed','Remaining'],title='Flashcard Progress',orientation='h',barmode='stack',text=[display_text],
                    color_discrete_map={'Completed':'green', 'Remaining':'whitesmoke'},width = 1000, height = 300)
            fig.update_layout(showlegend=False,xaxis_title='Total Flashcards available')
            fig.for_each_trace(lambda t: t.update(text = []) if t.name not in ['Remaining'] else ())
            st.write(fig)

    with tab4:
        @st.experimental_dialog("Create a custom practice test",width='large')
        def generate_pt():
            with st.container():
                st.write("Create a custom practice test from either topics or recommended document/questions!")
                selected_method = st.radio('Choose how to generate your practict tests', ['By Content','By Topics'],horizontal=True,index=None)
                if selected_method == 'By Content':
                    concept_list = []
                    st.markdown(''':blue[Select from documents or QA below you want to cover in the practice test below]''')
                    for res in doc_assets.keys():
                        if res<=4:
                            values = st.checkbox('document_'+str(res)+' document_title')
                        else:
                            values = st.checkbox('question_'+str(res)+' question_title')
                        if values:
                            concept_list.extend(fc_asset_to_topic_map[res])
                            concept_list = list(set(concept_list))
                    st.markdown(''':green[Topics covered with selected documents & questions]''')
                    for c in range(len(date_topic_mapping[nav.split(' ')[-1]])):
                        if c in concept_list:
                            st.markdown(f'''* {date_topic_mapping[nav.split(' ')[-1]][c]}''')
                    if st.button('Generate'):
                            st.write("Practice test generated successfully")
                            open_page(ai_test_prep_url)
                if selected_method == 'By Topics':
                    for res2 in date_topic_mapping[nav.split(' ')[-1]][1:]:
                        values2 = st.checkbox(res2)
                    if st.button('Generate'):
                            st.write("Practice test generated successfully")
                            open_page(ai_test_prep_url)    
        if st.button('Generate a custom practict test today'):
            generate_pt()

        with st.container():
            for indx,cols in enumerate(st.columns(4)):
                if indx<=3:
                    if indx_of_selected in asset_to_topic_map[indx+1]+[0]:
                        gif_html = get_img_with_href(f'streamlit_demo1/Assets/practice_problem_assets/PT{indx+1}.jpg',ai_test_prep_url)
                        cols.markdown(gif_html, unsafe_allow_html=True)
                else:
                    if indx_of_selected in asset_to_topic_map[indx+1]+[0]:
                        gif_html = get_img_with_href(f'streamlit_demo1/Assets/practice_problem_assets/PT{indx+1}_C.jpg',ai_test_prep_url)
                        cols.markdown(gif_html, unsafe_allow_html=True)
            for indx,cols in enumerate(st.columns(4)):
                if indx>=2:
                    # gif_html = get_img_with_href('streamlit_demo1/Assets/practice_problem_assets/FC_own.jpg',ai_test_prep_url)
                    # cols.markdown(gif_html, unsafe_allow_html=True)
                    break
                if indx_of_selected in asset_to_topic_map[indx+5]+[0]:
                    gif_html = get_img_with_href(f'streamlit_demo1/Assets/practice_problem_assets/PT{indx+5}_C.jpg',ai_test_prep_url)
                    cols.markdown(gif_html, unsafe_allow_html=True)
        tc1,tc2 = st.columns([1,3])
        # overall score 
        with tc1:
            d2 = {'score':[85],'text_score':'85%'}
            df = pd.DataFrame(d2)
            fig = px.bar(df,y='score',title='Overall score',text='text_score',width = 300, height = 500)
            fig.update_layout(showlegend=False,xaxis_title='Practice test score',yaxis_range=[0,100])
            st.write(fig)
        with tc2:
            d3={'topics':date_topic_mapping[nav.split(' ')[-1]][1:],
                'score':[66,33,88],
                'text_score':['66%','33%','88%'],
                }
            df = pd.DataFrame(d3)
            df.sort_values('score',ascending=False,inplace=True)
            fig = px.bar(df,y='topics',x='score',title='Topic score',text='text_score',color='topics',width = 1000, height = 500,orientation='h')
            fig.update_layout(showlegend=False,xaxis_title='Practice test score by topics',xaxis_range=[0,100])
            st.write(fig)

        d = {'Total':[6],'Completed':[2]}
        df=pd.DataFrame(d)
        df['Remaining'] = df['Total']-df['Completed']
        df['Progress'] = ((df['Completed']/df['Total'])*100).round(1)
        display_text = f"Completed: {df['Progress'][0]}%"
        fig = px.bar(df,y='Total',x=['Completed','Remaining'],title='Practice Test Progress',orientation='h',barmode='stack',text=[display_text],
                color_discrete_map={'Completed':'green', 'Remaining':'whitesmoke'},width = 1000, height = 300)
        fig.update_layout(showlegend=False,xaxis_title='Total Practice test available')
        fig.for_each_trace(lambda t: t.update(text = []) if t.name not in ['Remaining'] else ())
        st.write(fig)