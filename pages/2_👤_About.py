import streamlit as st

st.set_page_config(page_title="About", page_icon="👤", layout="wide")

st.markdown("""
<style>
    .about-card {
        background: #f0f4ff;
        padding: 30px;
        border-radius: 12px;
        margin: 20px 0;
        border-left: 4px solid #667eea;
    }
    .timeline-item {
        background: white;
        padding: 20px;
        margin: 15px 0;
        border-left: 4px solid #667eea;
        border-radius: 8px;
    }
    .section-title {
        font-size: 28px;
        font-weight: 700;
        color: #1e293b;
        margin: 30px 0 20px 0;
        border-bottom: 3px solid #667eea;
        padding-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.title("👤 About Me")

# Professional Summary
st.markdown('<div class="section-title">Professional Summary</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    I'm a **results-driven DevOps engineer** with a passion for building reliable, scalable, and secure cloud infrastructure. 
    My journey in technology has been driven by a desire to automate, optimize, and innovate.
    
    With **5+ years of hands-on experience**, I've successfully:
    - 🏗️ Architected multi-cloud infrastructure solutions
    - 🚀 Implemented CI/CD pipelines that reduced deployment time by 60%
    - 📈 Scaled systems to handle millions of requests
    - 🔒 Enhanced security posture through infrastructure hardening
    - 💰 Reduced cloud costs by 40% through optimization strategies
    
    I'm AWS Certified Professional and deeply experienced with Kubernetes, helping teams modernize their applications
    and embrace DevOps best practices.
    """)

with col2:
    st.image("https://via.placeholder.com/300x400?text=Professional+Photo", caption="Pankaj Jagdish", use_column_width=True)

# Education
st.markdown('<div class="section-title">Education & Certifications</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="timeline-item">
        <h4>AWS Certified Solutions Architect Professional</h4>
        <p>Amazon Web Services | 2023</p>
        <p>Demonstrated expertise in designing highly available, fault-tolerant, and scalable AWS solutions.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="timeline-item">
        <h4>AWS Certified DevOps Engineer Professional</h4>
        <p>Amazon Web Services | 2022</p>
        <p>Certified in implementing and managing CI/CD pipelines on AWS infrastructure.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="timeline-item">
        <h4>Kubernetes Application Developer</h4>
        <p>The Linux Foundation | 2021</p>
        <p>Proficient in designing and implementing containerized applications.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="timeline-item">
        <h4>Bachelor's in Computer Science</h4>
        <p>University | 2018</p>
        <p>Strong foundation in computer science fundamentals and software engineering principles.</p>
    </div>
    """, unsafe_allow_html=True)

# Core Competencies
st.markdown('<div class="section-title">Core Competencies</div>', unsafe_allow_html=True)

competencies = {
    "Cloud Platforms": ["AWS", "Azure", "GCP"],
    "Container Tech": ["Kubernetes", "Docker", "Helm"],
    "Infrastructure as Code": ["Terraform", "CloudFormation", "Ansible"],
    "CI/CD Tools": ["GitHub Actions", "Jenkins", "GitLab CI"],
    "Monitoring": ["Prometheus", "Grafana", "ELK Stack"],
    "Programming": ["Python", "Bash", "Go", "JavaScript"]
}

cols = st.columns(3)
for idx, (category, items) in enumerate(competencies.items()):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="about-card">
            <h4>{category}</h4>
            <p>{', '.join(items)}</p>
        </div>
        """, unsafe_allow_html=True)

# Philosophy
st.markdown('<div class="section-title">My Philosophy</div>', unsafe_allow_html=True)

st.markdown("""
I believe in:

🤝 **Collaboration** - DevOps is about breaking silos between teams and fostering collaboration

📚 **Continuous Learning** - Technology evolves rapidly, and staying updated is crucial

🎯 **Reliability** - Building systems that are resilient, observable, and maintainable

🔧 **Automation** - Automating repetitive tasks to focus on strategic initiatives

📊 **Data-Driven** - Using metrics and monitoring to make informed decisions
""")
