import streamlit as st

# Title of the app
st.title('Growth Mindset Challenge')

# Introduction section
st.header('What is a Growth Mindset?')
st.write("""
A growth mindset is the belief that your abilities and intelligence can be developed through hard work, perseverance, and learning from your mistakes. 
This concept was popularized by psychologist Carol Dweck, and it challenges the notion that our skills are fixed from the start. Instead, it reminds us that every challenge is an opportunity to learn and improve.
""")

# Why Adopt a Growth Mindset section
st.header('Why Adopt a Growth Mindset?')
st.write("""
- **Embrace Challenges**: View obstacles as opportunities to learn rather than as setbacks.
- **Learn from Mistakes**: Understand that making mistakes is a natural part of learning. Each error is a chance to improve.
- **Persist Through Difficulties**: Stay determined, even when things get tough. Hard work and persistence can lead to growth.
- **Celebrate Effort**: Recognize and reward the effort you put into learning, not just the final result.
- **Keep an Open Mind**: Stay curious and be willing to adapt your approach based on what you learn.
""")

# Interactive section: A quick quiz to check the user's mindset
st.header('Quick Mindset Quiz')

quiz_questions = {
    "Do you enjoy taking on challenges?": ["Yes", "No"],
    "Do you feel setbacks are a chance to learn?": ["Yes", "No"],
    "Do you ask for feedback to improve your skills?": ["Yes", "No"],
    "Do you believe effort is more important than talent?": ["Yes", "No"],
}

quiz_answers = {}

for question, options in quiz_questions.items():
    quiz_answers[question] = st.radio(question, options)

# Collecting responses and showing them
if st.button('Submit Answers'):
    st.write('Your Growth Mindset Quiz Results:')
    for question, answer in quiz_answers.items():
        st.write(f'{question}: {answer}')

# Conclusion and Encouragement
st.header('Next Steps to Foster a Growth Mindset')
st.write("""
- **Set Learning Goals**: Focus on developing new skills, not just grades.
- **Reflect on Your Progress**: Take time to assess what you've learned and how you've grown.
- **Embrace Feedback**: Use constructive feedback to improve yourself.
- **Stay Positive**: Always remember, you can grow with hard work and effort!
""")
