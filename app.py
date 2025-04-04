import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration for a better layout
# Adding Favicon
st.set_page_config(
    page_title = 'IPL Win Predictor',
    page_icon = '🏏',
)

# Define lists of IPL teams and host cities
teams = [
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bengaluru',
    'Kolkata Knight Riders', 'Punjab Kings', 'Chennai Super Kings',
    'Rajasthan Royals', 'Delhi Capitals', 'Gujarat Titans', 
    'Lucknow Super Giants'
]

cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
    'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
    'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali', 'Bengaluru', 'Lucknow'
]

# Load the pre-trained model for win probability prediction
pipe = pickle.load(open('pipe_new.pkl', 'rb'))

# Streamlit title with custom styling
st.markdown(
    """
    <style>
    .title {
        font-size: 2.5em;  /* Set title font size */
        color: #FFD700;    /* Gold color for the title */
        text-align: center; /* Center the title */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the title
st.markdown('<h1 class="title">🌟 IPL Win Predictor 🌟</h1>', unsafe_allow_html=True)

# Create a main container for input fields
with st.container():

    # Create columns for selecting batting and bowling teams
    col1, col2 = st.columns(2)

    with col1:
        batting_team = st.selectbox('Select the batting team', sorted(teams), index=0)  # Dropdown for batting team
    with col2:
        bowling_team = st.selectbox('Select the bowling team', sorted(teams), index=1)  # Dropdown for bowling team

    # Dropdown to select the host city
    selected_city = st.selectbox('Select host city', sorted(cities))

    # Input for target score
    target = st.number_input('Target', min_value=1, step=1, format="%d")  # Input for target score

    # Create columns for score, overs, and wickets
    col3, col4, col5 = st.columns(3)

    with col3:
        score = st.number_input('Score', min_value=0, step=1, format="%d")  # Input for current score
    with col4:
        overs = st.number_input('Overs completed', min_value=0, step=1, format="%d")  # Input for overs completed
    with col5:
        wickets = st.number_input('Wickets out', min_value=0, step=1, format="%d")  # Input for wickets lost

    # Button to predict win probabilities
    if st.button('Predict Probability', key='predict_button', help='Click to predict win probabilities'):
        # Calculate parameters for prediction
        runs_left = target - score  # Runs left to chase
        balls_left = 120 - (overs * 6)  # Total balls left in the innings
        wickets_remaining = 10 - wickets  # Remaining wickets
        crr = score / overs if overs > 0 else 0  # Current run rate
        rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0  # Required run rate

        # Prepare input DataFrame for prediction
        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [selected_city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets': [wickets_remaining],
            'total_runs_x': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        # Get prediction results from the model
        result = pipe.predict_proba(input_df)
        loss = result[0][0]  # Probability of the bowling team winning
        win = result[0][1]   # Probability of the batting team winning

        # Display win probabilities
        st.header(f"{batting_team} - {round(win * 100, 2)}%")  # Display batting team's win probability
        st.header(f"{bowling_team} - {round(loss * 100, 2)}%")  # Display bowling team's win probability

        # Prepare data for visualization
        teams = [batting_team, bowling_team]  # List of teams
        win_probabilities = [win * 100, loss * 100]  # Win probabilities as percentages

        # Create a bar plot using seaborn
        plt.figure(figsize=(10, 6))
        sns.set(style="whitegrid")  # Set the background style for the plot

        # Use an elegant color palette for the bars
        palette = sns.color_palette("muted", n_colors=len(teams))
        sns.barplot(x=teams, y=win_probabilities, palette=palette)

        # Set y-axis label and title
        plt.ylabel('Win Probability (%)', fontsize=16, fontweight='bold', labelpad=10)  # Y-axis label
        plt.title('Predicted Win Probabilities', fontsize=20, fontweight='bold', pad=20)  # Plot title
        plt.xticks(rotation=45, ha='right', fontsize=14)  # X-axis tick labels
        plt.yticks(fontsize=12)  # Y-axis tick labels
        plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add horizontal grid lines
        plt.gca().spines['top'].set_visible(False)  # Hide the top spine
        plt.gca().spines['right'].set_visible(False)  # Hide the right spine
        plt.ylim(0, 100)  # Set y-axis limits

        # Add data labels on top of the bars for clarity
        for index, value in enumerate(win_probabilities):
            plt.text(index, value + 1, f'{value:.1f}%', ha='center', fontsize=12)

        # Display the plot in Streamlit
        st.pyplot(plt)
