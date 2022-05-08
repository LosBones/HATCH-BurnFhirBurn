#Imports
import streamlit as st
import pandas as pd
import altair as alt
from fhirclient import client
import fhirclient.models.patient as p
import pygame
pygame.font.init()
import pandas
import json
import time

WhichWhich=3
leftClick=False
rightClick=False

#fontTitels = pygame.font.SysFont('impact', 40)
# text_surface = my_font.render("Test", False, (0, 0, 0))
# screen1.blit(text_surface, (335,535))
# pygame.draw.rect(screen1, (0,0,0), pygame.Rect(300, 200, 150, 200))


screen2=pygame.display.set_mode((225, 100))
Screen2color=(161, 140, 148)
screen2.fill(Screen2color)
StartingScreenRun=True

pygame.draw.rect(screen2, (0,0,0), pygame.Rect(25,25,75,50))
pygame.draw.rect(screen2, (0,0,0), pygame.Rect(125,25,75,50))
pygame.draw.rect(screen2, (255,255,255), pygame.Rect(30,30,65,40))
pygame.draw.rect(screen2, (255,255,255), pygame.Rect(130,30,65,40))

MenuFont=pygame.font.SysFont('impact', 20)

text_surface = MenuFont.render("Send", False, (0, 0, 0))
screen2.blit(text_surface, (42,37))

text_surface = MenuFont.render("Recive", False, (0, 0, 0))
screen2.blit(text_surface, (135,37))

while StartingScreenRun==True:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                leftClick = True
            if event.button == 3:
                rightClick = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                leftClick = False
            if event.button == 3:
                rightClick = False
    if leftClick == True and 30<mouse[0]<95and 30<mouse[1]<70:
        StartingScreenRun =False
        WhichWhich=0
    if leftClick == True and 130<mouse[0]<195and 30<mouse[1]<70:
        StartingScreenRun =False
        WhichWhich=1
    if event.type == pygame.QUIT:
            StartingScreenRun =False

    pygame.display.update()

if WhichWhich==0:
    #Imports
    from fhirclient import client
    import fhirclient.models.patient as p
    import pygame
    pygame.font.init()
    import pandas
    import json
    import time

    #Setting the app that gets called from
    settings = {
        'app_id': 'my_web_app',
        'api_base': 'http://wildfhir4.aegis.net/fhir4-0-1'
    }

    #Defining the call of the client
    smart = client.FHIRClient(settings=settings)

    #Takes client Info and reads it
    patient = p.Patient.read('f001', smart.server)

    #Creates list of client info
    TheData=[
    "First Name : " + str(patient.name[0].given[0]),
    "Last Name : " + str(patient.name[0].family),
    "Active : " + str(patient.active),
    "BirthDate : " + str(patient.birthDate.isostring),
    "Contact : " + str(patient.contact[0].telecom[0].use),
    "Gender : " + str(patient.gender),
    "Practiciner : " + str(patient.generalPractitioner),
    "ID : " + str(patient.id),
    ]

    #Making Screen for pygame
    screen1=pygame.display.set_mode((500, 600))
    Screen1color=(161, 140, 148)
    screen1.fill(Screen1color)
    ButtonStart=90

    #Varibles for Pygame
    run=True
    leftClick=False
    rightClick=False
    Gene="Gene Test"
    Blood="Blood Test"
    Drug="Drug Test"
    TestList=[]
    TestDisplayCounter=240
    TestDisplayTrue=False

    #Rectangles for buttons
    def Buttons(StartX,StartY,InsideColor,OutsideColor):
        pygame.draw.rect(screen1, OutsideColor, pygame.Rect(StartX, StartY, 100, 100))
        pygame.draw.rect(screen1, InsideColor, pygame.Rect(StartX+10, StartY+10, 80, 80))
    Buttons(ButtonStart,490,(255,255,255),(0,0,0))
    Buttons(ButtonStart+110,490,(255,255,255),(0,0,0))
    Buttons(ButtonStart+220,490,(255,255,255),(0,0,0))

    #Person Info
    my_font = pygame.font.SysFont('Comic Sans MS', 20)
    for y in range(0,len(TheData)):
        text_surface = my_font.render(TheData[y], False, (0, 0, 0))
        screen1.blit(text_surface, (50,50*y+55))

    #Catigory Labels
    my_fontTitels = pygame.font.SysFont('impact', 40)

    text_surface = my_fontTitels.render("Patient Info", False, (0, 0, 0))
    screen1.blit(text_surface, (150,10))

    text_surface = my_fontTitels.render("Orderable Tests", False, (0, 0, 0))
    screen1.blit(text_surface, (140,440))

    #Labels on buttons
    my_fontLabels = pygame.font.SysFont('cambria', 8)
    text_surface = my_font.render("Gene", False, (0, 0, 0))
    screen1.blit(text_surface, (115,510))
    text_surface = my_font.render("Test", False, (0, 0, 0))
    screen1.blit(text_surface, (115,535))

    text_surface = my_font.render("Blood", False, (0, 0, 0))
    screen1.blit(text_surface, (225,510))
    text_surface = my_font.render("Test", False, (0, 0, 0))
    screen1.blit(text_surface, (225,535))

    text_surface = my_font.render("Drug", False, (0, 0, 0))
    screen1.blit(text_surface, (335,510))
    text_surface = my_font.render("Test", False, (0, 0, 0))
    screen1.blit(text_surface, (335,535))

    #Submit Area
    pygame.draw.rect(screen1, (0,0,0), pygame.Rect(300, 200, 150, 200))
    pygame.draw.rect(screen1, (255,255,255), pygame.Rect(310, 210, 130, 180))

    #Submit/ClearButton
    pygame.draw.rect(screen1, (0,0,0), pygame.Rect(300, 150, 150, 50))
    pygame.draw.rect(screen1, (255,255,255), pygame.Rect(310, 160, 130, 40))
    pygame.draw.rect(screen1, (0,0,0), pygame.Rect(372, 150, 6, 50))

    #Displaying ordered test
    my_fontSubmitArea = pygame.font.SysFont('impact', 20)
    text_surface = my_fontSubmitArea.render("Ordered Tests", False, (0, 0, 0))
    screen1.blit(text_surface, (320,210))

    #Buttons for Clearing/Submitting
    text_surface = my_fontSubmitArea.render("Submit", False, (0, 0, 0))
    screen1.blit(text_surface, (313,165))
    text_surface = my_fontSubmitArea.render("Clear", False, (0, 0, 0))
    screen1.blit(text_surface, (385,165))

    #Exit Button
    pygame.draw.rect(screen1, (0,0,0), pygame.Rect(0, 570, 50, 30))
    pygame.draw.rect(screen1, (255,255,255), pygame.Rect(0, 575, 45, 20))
    my_fontExit = pygame.font.SysFont('impact', 15)
    text_surface = my_fontExit.render("Close", False, (0, 0, 0))
    screen1.blit(text_surface, (5,577))

    while run==True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    leftClick = True
                if event.button == 3:
                    rightClick = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    leftClick = False
                if event.button == 3:
                    rightClick = False
        if leftClick == True and 90<mouse[0]<190 and 490<mouse[1]<590:
            RequestedTest="GeneTest"
            TestDisplayTrue=True
            TestList.append(Gene)
        elif leftClick == True and 200<mouse[0]<300 and 490<mouse[1]<590:
            RequestedTest="BloodTest"
            TestDisplayTrue=True
            TestList.append(Blood)
        elif leftClick == True and 310<mouse[0]<410 and 490<mouse[1]<590:
            RequestedTest="DrugTest"
            TestDisplayTrue=True
            TestList.append(Drug)
        elif leftClick == True and 310<mouse[0]<372 and 160<mouse[1]<200 and len(TestList)>0:
            run =False
        elif leftClick == True and 372<mouse[0]<450 and 160<mouse[1]<200:
            TestList.clear()
            pygame.draw.rect(screen1, (255,255,255), pygame.Rect(310, 235, 130, 155))
        elif leftClick == True and 0<mouse[0]<45 and 575<mouse[1]<595:
            run =False
        if event.type == pygame.QUIT:
                run =False
        if TestDisplayTrue==True:
            TestDisplayTrue=False
            for i in range(0,len(TestList)):
                if i*25+TestDisplayCounter<370:
                    text_surface = my_font.render(TestList[i], False, (0, 0, 0))
                    screen1.blit(text_surface, (320,i*25+TestDisplayCounter))
            time.sleep(0.3)


        pygame.display.update()

    patient.__dict__['testrequested'] = TestList
    print(patient.__dict__)



if WhichWhich==1:
    st.write("Hello, Doctor Paul!")
    from urllib.error import URLError
    import base64
    page = st.selectbox("Choose your box", ["Main Page", "Notifications"])
    if page == "Main Page":
        #Display destails of Main


        patient_number = st.text_input('Patient account number', 'AOO1244-3-03')
        st.write('Current patient number', patient_number)
        try:
            ordertype = st.multiselect("Please select",
                ["PDF", "CSV"]
            )
            if not ordertype:
                st.error("Please select one copy.")
            else:
                st.write(ordertype)
                uploaded_file = st.file_uploader("Choose a file",accept_multiple_files=False)
                if uploaded_file is not None:
                    st.write("fileuploaded successfully")
                    # # To read file as bytes:
                    # bytes_data = uploaded_file.getvalue()
                    # st.write(bytes_data)

                    # To convert to a string based IO:
                    base64_pdf = base64.b64encode(uploaded_file.read())
                    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf.decode("utf-8")}" width="700" height="1000" type="application/pdf"></iframe>'
                    st.markdown(pdf_display, unsafe_allow_html=True)
                    import time
                    my_bar = st.progress(0)
                    for percent_complete in range(100):
                        time.sleep(0.1)
                    my_bar.progress(percent_complete + 1)

                    # # To read file as string:
                    # string_data = stringio.read()
                    # st.write(string_data)

                    # # Can be used wherever a "file-like" object is accepte

                # data = df.loc[File types]
                # data /= 1000000.0
                # st.write("### Gross Agricultural Production ($B)", data.sort_index())

                # data = data.T.reset_index()
                # data = pd.melt(data, id_vars=["index"]).rename(
                #     columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
                # )
                # chart = (
                #     alt.Chart(data)
                #     .mark_area(opacity=0.3)
                #     .encode(
                #         x="year:T",
                #         y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                #         color="Region:N",
                #     )
                # )
                # st.altair_chart(chart, use_container_width=True)
        except URLError as e:
            st.error(
                """
                **This demo requires internet access.**
    
                Connection error: %s
            """
                % e.reason
            )

    elif page == "Notifications":
        #Display details of Notifications
        st.write("Notifications")
        text_input = st.text_input("Tana Smith (Completed)", "Kennan Stokes (Pending)")


