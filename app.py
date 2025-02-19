import streamlit as st
import matplotlib.pyplot as plt
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from streamlit_option_menu import option_menu

# Email credentials
smtp_server = "smtp.office365.com"
smtp_port = 587
smtp_user = "support@aptpath.in"
smtp_password = "kjydtmsbmbqtnydk"
sender_email = "support@aptpath.in"
receiver_emails = ["saketh1805@gmail.com"] 

# Function to send feedback via email
def send_feedback_email(name, email, message):
    try:
        # Create the email content
        subject = "New Feedback Received"
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = ", ".join(receiver_emails)
        msg["Subject"] = subject

        body = f"""
        You have received a new feedback:

        Name: {name}
        Email: {email}

        Message:
        {message}
        """
        msg.attach(MIMEText(body, "plain"))

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(sender_email, receiver_emails, msg.as_string())
        
        return True
    except Exception as e:
        st.error(f"Error sending email: {e}")
        return False

# Function to save feedback to a CSV file
def save_feedback(name, email, message):
    with open("feedback.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, message])

# CSS for background image 
def add_bg_from_url(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Home Page
def home_page():
    add_bg_from_url("https://images.unsplash.com/photo-1530569673472-307dc017a82d?q=80&w=1888&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")  # Background for Home page
    
    st.title("Interactive Air Quality Insights")
    st.write("""  
            Air quality has a direct impact on our health and the environment. In an age of
              rapid industrialization and urbanization, understanding the Air Quality Index (AQI) 
             is crucial for making informed decisions. This platform provides comprehensive insights
              into air quality levels across regions, empowering users to protect their health and contribute to a cleaner environment.
             """)
    st.header("What is AQI?")
    st.info("Sign in to continue.")

    st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: #81D4FA; /* Set button background color */
        color: white; /* Set text color */
        border-radius: 10px; /* Optional: Add rounded corners */
        border: 1px solid white; /* Optional: Add a white border */
        font-size: 16px; /* Optional: Adjust font size */
        padding: 8px 20px; /* Optional: Adjust padding */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

    if st.button("Sign In"):
        st.session_state.page = "register"

# Register Page
def register_page():
    add_bg_from_url("https://media.istockphoto.com/id/1427541414/vector/internet-digital-security-technology-concept-for-business-background-lock-on-circuit-board.jpg?s=612x612&w=0&k=20&c=eo94YzhlPOS2EYKnIppgK0f5-omfU3QCDOErlEghPBg=")  # Background for Login page
    st.title("Register")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if username and email and password:
            st.session_state.user = {"username": username, "email": email, "password": password}
            st.session_state.page = "login"
            st.success("Registration successful! Please log in.")
        else:
            st.error("Please fill in all fields.")

    st.markdown("Already have an account? ", unsafe_allow_html=True)
    if st.button("Go to Login"):
        st.session_state.page = "login"

# Login Page
def login_page():
    add_bg_from_url("https://media.istockphoto.com/id/1427541414/vector/internet-digital-security-technology-concept-for-business-background-lock-on-circuit-board.jpg?s=612x612&w=0&k=20&c=eo94YzhlPOS2EYKnIppgK0f5-omfU3QCDOErlEghPBg=")  # Background for Login page
    
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = st.session_state.get("user")
        if user and user.get("email") == email and user.get("password") == password:
            st.session_state.page = "report"
            st.success("Login successful! Redirecting...")
        else:
            st.error("Invalid email or password.")

    st.markdown("Don't have an account? ", unsafe_allow_html=True)
    if st.button("Go to Register"):
        st.session_state.page = "register"

def report_page():
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvUbloRvWHspNLvVDLHGkLOzzP52v7tPT4Tg&s'); /* Replace with your image path */
            background-size: cover; /* Ensure the image covers the sidebar */
            background-repeat: no-repeat; /* Avoid repeating the image */
            background-position: center; /* Center the image */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] h1 {
            color:white ; /* Change to desired color */
            font-size: 30px; /* Adjust font size as needed */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.title("Welcome Back!")
    with st.sidebar:
        choice = option_menu(
            menu_title=None,
            options=["Home", "Dashboard", "Conclusion", "Feedback"],
            icons=['house-fill', 'bar-chart-line-fill', 'easel3-fill', 'chat-left-text-fill'],
            menu_icon='None',
            default_index=0,
            styles={
                "container": {"padding": "2!important", "background-color": "#606060"},
                "icon": {"color": "white", "font-size": "23px"},
                "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "1px", "--hover-color": "#808080"},
                "nav-link-selected": {"background-color": "#202020"},
            }
        )

        st.sidebar.markdown("---")
        st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: #3C3D37; /* Set button background color */
        color: white; /* Set text color */
        border-radius: 10px; /* Optional: Add rounded corners */
        border: 1px solid white; /* Optional: Add a white border */
        font-size: 16px; /* Optional: Adjust font size */
        padding: 8px 20px; /* Optional: Adjust padding */
    }
    div.stButton > button:hover {
        background-color: grey; /* Change color on hover */
        color: white; /* Optional: Change text color on hover */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

        if st.sidebar.button("Logout"):
            st.session_state.page = "home"

    if choice == "Home":
        # Main header with a styled title
        add_bg_from_url("https://images.unsplash.com/photo-1530569673472-307dc017a82d?q=80&w=1888&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")  # Background for Home page

        st.markdown("<h1 style='text-align: center; color: #4CAF50;'>ClearView-Interactive Air Quality Insights</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color:rgb(24, 23, 23);'>Empowering communities with actionable air quality data</h4>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; color:rgb(10, 10, 10);font-size: 25px'><em>Breathe Easy, Stay Informed.</em></h6>", unsafe_allow_html=True)
        st.markdown("---")
        # Introduction Section
        with st.container():
            st.header("Introduction")
            st.info("""
            The ClearView Air Quality Insights Dashboard is designed to empower users with a deeper understanding of air quality across various regions. This project uses historical data on Air Quality Index (AQI) and key pollutants such as PM2.5, PM10, NO2, SO2, and O3 to provide meaningful insights. With data sourced from real-world observations, ClearView aims to bridge the gap between raw data and actionable insights, enabling users to make informed decisions about environmental quality
            """)
        
       # Project Overview Section
        st.markdown("<h2 style='color: #4CAF50;font-size: 25px'>🌟 Project Overview</h2>", unsafe_allow_html=True)
        st.markdown("""
       ClearView is an innovative project designed to provide comprehensive air quality insights through an advanced interactive dashboard. By harnessing historical air quality and meteorological data, ClearView aims to transform complex datasets into accessible and actionable visualizations, empowering users to understand and respond to environmental challenges effectively.
        """)
        
        # Objectives Section
        st.markdown("<h2 style='color: #4CAF50;font-size: 25px'>🎯 Objectives</h2>", unsafe_allow_html=True)
        st.markdown("""
        - **Visualize Air Quality Index (AQI) trends** and pollutant levels across various regions.
        - **Enable users to explore historical data, monitor changes,** and identify regional disparities in air quality.
        - **Provide actionable insights and forecasts** to support informed decision-making by individuals, organizations, and policymakers.
        """)

        # Mission Section
        st.markdown("<h2 style='color: #4CAF50;font-size: 25px'>🚀 Mission</h2>", unsafe_allow_html=True)
        st.markdown("""
        ClearView's mission is to promote environmental awareness and proactive engagement by delivering intuitive tools that simplify air quality analysis. 
        Through this platform, we aspire to foster healthier communities and encourage sustainable practices for a cleaner future.
        """)

        # Comprehensive and User-Friendly Platform Section
        st.markdown("<h2 style='color: #4CAF50;font-size: 25px'>💻 A Comprehensive and User-Friendly Platform</h2>", unsafe_allow_html=True)
        st.write("""
        The dashboard leverages interactive visualizations to allow users to analyze AQI trends over time, monitor changes, 
        and compare air quality across different regions. Embedded within a Streamlit web application, the platform ensures 
        an intuitive and accessible interface suitable for environmental analysts, policymakers, and the general public. 
        Users can effortlessly explore air quality disparities, historical trends, and regional insights, fostering a better 
        understanding of how air quality evolves and its implications.
        """)

        # Reliable and Actionable Insights Section
        st.markdown("<h2 style='color: #4CAF50;font-size: 25px'>🔍 Reliable and Actionable Insights</h2>", unsafe_allow_html=True)
        st.write("""
        As part of the development process, the data is meticulously preprocessed and structured to ensure accuracy and relevance. 
        The final dashboard undergoes comprehensive testing to validate its functionality and reliability, ensuring a seamless user experience. 
        Detailed documentation accompanies the project, supporting both immediate use and future enhancements. 
        ClearView is not just a tool but a step towards promoting environmental awareness and action.
        """)
        # Footer with centered text
        st.markdown("---")
        st.markdown("<p style='text-align: center;font-size: 20px'>🌍 Let's work together for a cleaner, greener future! 🌱</p>", unsafe_allow_html=True)

    elif choice == "Dashboard":
        add_bg_from_url("https://images.unsplash.com/photo-1530569673472-307dc017a82d?q=80&w=1888&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")  # Background for Home page
        st.title("Real-Time Air Quality Data")
        st.write("""Our Real-Time Air Quality Dashboard provides you with live updates and detailed insights on air quality.
                  Whether you’re at home, work, or traveling,staying informed about the AQI in your area is essential for making health-conscious decisions.""")
        st.header("Interactive AQI Visualizations")
        st.markdown("""
                    With the help of our interactive dashboard, you can view:
- **Historical Trends**: Track how air quality has changed over time with historical data charts.
- **Pollutant Breakdown**: Dive into the specific pollutants contributing to poor air quality, such as PM2.5, PM10, and NO2.
- **Comparative Analysis**: Compare air quality across multiple locations to see how different areas are affected by pollution.                   
""")
        st.write("Explore the Air Quality Index data through the embedded Power BI dashboard below:")

        Dashboard = """
                    <iframe title="Air Quality Index" 
                            width="700" 
                            height="500" 
                            src="https://app.powerbi.com/view?r=eyJrIjoiZDZlMjhjMzMtYjI3ZC00ZTE2LWIzNWMtMzljYjE5NTQzZjI4IiwidCI6IjcyNDBlMzY3LTY0YTgtNDkyYy1iNDIwLThhNWU2ZDRmNjViZCJ9&pageName=1a249e5339039b2ce3a9" 
                            frameborder="0" 
                            allowFullScreen="true">
                    </iframe>
                        """

        st.components.v1.html(Dashboard, height=500)

    elif choice == "Conclusion":
        add_bg_from_url("https://images.unsplash.com/photo-1530569673472-307dc017a82d?q=80&w=1888&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")  # Background for Home page
        st.markdown("<h2 style=color: #2A3F54;'>Conclusion📖</h2>", unsafe_allow_html=True)
        st.markdown("""
        <div style='padding: 15px; border-radius: 8px;'>
            <p style='font-size: 18px; color: #333;'>
                Air quality remains a <b>critical issue</b> in India, with significant disparities observed across regions.
            </p>
            <ul style='font-size: 16px; color: #555;'>
                <li>States like <b>Uttar Pradesh, Punjab, and Rajasthan</b> show consistently high pollutant levels, particularly PM10 and PM2.5.</li>
                <li>Southern states like <b>Kerala and Karnataka</b> exhibit comparatively cleaner air.</li>
                <li>Major cities such as <b>New Delhi, Kochi, and Ahmedabad</b> are among the most polluted, requiring urgent action.</li>
            </ul>
            <p style='font-size: 18px; color: #333;'>
                Over the years, there has been some improvement, especially in <b>2022</b>, but the average AQI levels remain high, signaling persistent air quality issues. Pollutants like <b>SO2, NO2, and O3</b> show upward trends, further exacerbating the crisis.
            </p>
            <h3 style='color: #2A3F54;'>Key Recommendations:</h3>
            <ul style='font-size: 16px; color: #555;'>
                <li>Implement <b>targeted pollution control measures</b> in high-risk areas.</li>
                <li>Strengthen regulations to curb particulate matter (PM10, PM2.5) and harmful gases.</li>
                <li>Promote <b>public awareness</b> and adopt cleaner technologies.</li>
            </ul>
            <p style='font-size: 16px; color: #333;'>
                A tailored approach is essential to improve air quality and protect public health across India.
            </p>
        </div>
        """, unsafe_allow_html=True)
    elif choice == "Feedback":
        add_bg_from_url("https://images.unsplash.com/photo-1530569673472-307dc017a82d?q=80&w=1888&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")  # Background for Home page
        st.title("Feedback")
        st.write("Have questions or feedback? Fill out the form below:")

        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message")
            submitted = st.form_submit_button("Submit")

            if submitted:
                save_feedback(name, email, message)
                if send_feedback_email(name, email, message):
                    st.success("Thank you for reaching out! Your feedback has been sent successfully.")
                else:
                    st.error("Failed to send feedback email.")

        st.info("You can contact us by sharing your feedback in the Feedback section.")

# Routing Logic
def main():
    if "page" not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        home_page()
    elif st.session_state.page == "register":
        register_page()
    elif st.session_state.page == "login":
        login_page()
    elif st.session_state.page == "report":
        report_page()

if __name__ == "__main__":
    main()
