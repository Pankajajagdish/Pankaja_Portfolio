import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="Pankaj Jagdish - DevOps Engineer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    /* Main styling */
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main {
        background-color: #ffffff;
    }
    
    /* Hero section styling */
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 60px 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 40px;
    }
    
    .hero-title {
        font-size: 48px;
        font-weight: 700;
        margin: 20px 0;
    }
    
    .hero-subtitle {
        font-size: 24px;
        font-weight: 500;
        margin: 10px 0;
    }
    
    .hero-description {
        font-size: 18px;
        opacity: 0.9;
        margin: 15px 0;
    }
    
    /* Section titles */
    .section-title {
        font-size: 32px;
        font-weight: 700;
        color: #1e293b;
        border-bottom: 4px solid #6366f1;
        padding-bottom: 15px;
        margin: 40px 0 30px 0;
    }
    
    /* Skill tags */
    .skill-tag {
        background: #f8fafc;
        color: #6366f1;
        padding: 8px 16px;
        border-radius: 20px;
        border: 1px solid #6366f1;
        font-size: 14px;
        display: inline-block;
        margin: 5px;
    }
    
    /* Project cards */
    .project-card {
        background: #f8fafc;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #6366f1;
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(99, 102, 241, 0.1);
    }
    
    .project-title {
        font-size: 20px;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 10px;
    }
    
    .project-desc {
        color: #64748b;
        margin-bottom: 15px;
        line-height: 1.6;
    }
    
    .project-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
    }
    
    .tag {
        background: white;
        color: #6366f1;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 12px;
        border: 1px solid #6366f1;
    }
    
    /* Stat boxes */
    .stat-box {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin: 10px;
    }
    
    .stat-number {
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    
    .stat-label {
        font-size: 14px;
        opacity: 0.9;
    }
    
    /* Contact form */
    .contact-section {
        background: #f8fafc;
        padding: 30px;
        border-radius: 10px;
        margin-top: 40px;
    }
    
    /* Links */
    a {
        color: #6366f1;
        text-decoration: none;
    }
    
    a:hover {
        color: #ec4899;
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <div class="hero-title">Hi, I'm Pankaj Jagdish 👋</div>
    <div class="hero-subtitle">DevOps & Cloud Infrastructure Engineer</div>
    <div class="hero-description">AWS Certified | Kubernetes Specialist | CI/CD Expert</div>
    <p style="font-size: 18px; margin-top: 20px;">Automating infrastructure, optimizing CI/CD pipelines, and building scalable cloud solutions</p>
</div>
""", unsafe_allow_html=True)

# About Section
st.markdown('<div class="section-title">📋 About Me</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.write("""
    I'm a results-driven DevOps engineer passionate about automating infrastructure, optimizing CI/CD pipelines, and building scalable cloud solutions. 
    With expertise in AWS, Azure, Docker, Kubernetes, and Infrastructure as Code, I help teams deliver software efficiently and reliably.
    
    I specialize in designing and implementing robust DevOps solutions, managing containerized workloads at scale, and implementing best practices in cloud infrastructure. 
    My goal is to create automated, secure, and cost-optimized cloud environments that empower development teams.
    """)
    
    # Stats
    st.markdown("### Experience Metrics")
    metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
    
    with metrics_col1:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">5+</div>
            <div class="stat-label">Years DevOps Experience</div>
        </div>
        """, unsafe_allow_html=True)
    
    with metrics_col2:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">100+</div>
            <div class="stat-label">Infrastructure Deployments</div>
        </div>
        """, unsafe_allow_html=True)
    
    with metrics_col3:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">AWS</div>
            <div class="stat-label">Certified Professional</div>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 50%; 
                width: 250px; 
                height: 250px; 
                display: flex; 
                align-items: center; 
                justify-content: center;
                font-size: 80px;
                color: white;">
        🖥️
    </div>
    """, unsafe_allow_html=True)

# Skills Section
st.markdown('<div class="section-title">🛠️ Technical Skills</div>', unsafe_allow_html=True)

skills_data = {
    "☁️ Cloud Platforms": ["AWS", "Azure", "GCP", "CloudFormation", "Bicep"],
    "🐳 Container & Orchestration": ["Kubernetes", "AKS", "Docker", "Helm", "Container Registry"],
    "🔄 CI/CD & Automation": ["GitHub Actions", "Azure DevOps", "Jenkins", "Terraform", "Ansible"],
    "📊 Monitoring & Logging": ["Prometheus", "Grafana", "Azure Monitor", "Log Analytics", "ELK Stack"],
    "🐍 Programming Languages": ["Python", "Bash", "JavaScript", "YAML", "Go"],
    "⚙️ Additional Expertise": ["Linux", "Git", "RBAC", "Security", "Cost Optimization"]
}

for category, skills in skills_data.items():
    st.subheader(category)
    skill_html = ""
    for skill in skills:
        skill_html += f'<span class="skill-tag">{skill}</span>'
    st.markdown(skill_html, unsafe_allow_html=True)
    st.write("")

# Projects Section
st.markdown('<div class="section-title">🚀 Featured Projects</div>', unsafe_allow_html=True)

projects = [
    {
        "title": "GitHub Actions CI/CD Workflows",
        "description": "Production-ready CI/CD pipelines for automated testing, building, and deploying applications to AWS and Kubernetes.",
        "technologies": ["GitHub Actions", "Docker", "AWS", "Kubernetes"],
        "links": {
            "View Project": "https://github.com/Pankajajagdish/Github-actions-Projects-",
            "GitHub Profile": "https://github.com/Pankajajagdish"
        }
    },
    {
        "title": "Kubernetes AKS Infrastructure",
        "description": "Enterprise-grade Kubernetes cluster on Azure with advanced networking, RBAC, monitoring, and auto-scaling capabilities.",
        "technologies": ["Kubernetes", "AKS", "Terraform", "Azure"],
        "links": {
            "Documentation": "#",
            "Code": "https://github.com/Pankajajagdish"
        }
    },
    {
        "title": "Multi-Cloud Monitoring Stack",
        "description": "Integrated monitoring solution with Prometheus, Grafana, and Azure Log Analytics for distributed systems observability.",
        "technologies": ["Prometheus", "Grafana", "Azure Monitor", "Kubernetes"],
        "links": {
            "Architecture": "#",
            "GitHub": "#"
        }
    },
    {
        "title": "Infrastructure as Code Automation",
        "description": "Complete IaC solution using Terraform for provisioning and managing cloud resources across AWS and Azure with best practices.",
        "technologies": ["Terraform", "CloudFormation", "Python", "Azure"],
        "links": {
            "Repository": "#",
            "Documentation": "#"
        }
    },
    {
        "title": "Container Orchestration Platform",
        "description": "Advanced Kubernetes cluster management with Helm charts, service mesh integration, and automated scaling policies.",
        "technologies": ["Kubernetes", "Helm", "Docker", "GitOps"],
        "links": {
            "Architecture Docs": "#",
            "GitHub": "#"
        }
    },
    {
        "title": "Cloud Cost Optimization",
        "description": "Cost analysis and optimization framework for multi-cloud environments with automated tagging and resource management.",
        "technologies": ["Python", "AWS", "Azure", "Cost Analysis"],
        "links": {
            "Tools": "#",
            "GitHub": "#"
        }
    }
]

for project in projects:
    st.markdown(f"""
    <div class="project-card">
        <div class="project-title">{project['title']}</div>
        <div class="project-desc">{project['description']}</div>
        <div class="project-tags">
    """, unsafe_allow_html=True)
    
    for tech in project['technologies']:
        st.markdown(f'<span class="tag">{tech}</span>', unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)
    
    # Links
    link_cols = st.columns(len(project['links']))
    for idx, (link_text, url) in enumerate(project['links'].items()):
        with link_cols[idx]:
            st.markdown(f"[🔗 {link_text}]({url})")

# Contact Section
st.markdown('<div class="section-title">📧 Get In Touch</div>', unsafe_allow_html=True)

contact_col1, contact_col2 = st.columns(2)

with contact_col1:
    st.subheader("Send Me a Message")
    
    with st.form("contact_form"):
        name = st.text_input("Your Name", placeholder="John Doe")
        email = st.text_input("Your Email", placeholder="john@example.com")
        message = st.text_area("Your Message", placeholder="Tell me about your project...", height=150)
        submitted = st.form_submit_button("Send Message", use_container_width=True)
        
        if submitted:
            if name and email and message:
                st.success("✅ Message sent successfully! I'll get back to you soon.")
            else:
                st.error("❌ Please fill in all fields")

with contact_col2:
    st.subheader("Contact Information")
    
    st.markdown("""
    📧 **Email**: your.email@example.com
    
    📱 **Phone**: +1 (555) 123-4567
    
    📍 **Location**: United States
    
    ### Connect With Me
    """)
    
    social_cols = st.columns(4)
    with social_cols[0]:
        st.markdown("[🐙 GitHub](https://github.com/Pankajajagdish)")
    with social_cols[1]:
        st.markdown("[💼 LinkedIn](https://linkedin.com/in/pankajajagdish)")
    with social_cols[2]:
        st.markdown("[🐦 Twitter](https://twitter.com/yourhandle)")
    with social_cols[3]:
        st.markdown("[💻 Portfolio](https://github.com/Pankajajagdish)")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; padding: 20px;">
    <p>© 2024 Pankaj Jagdish. All rights reserved. | DevOps & Cloud Infrastructure Engineer</p>
    <p>Hosted on <strong>Streamlit Cloud</strong> ☁️</p>
</div>
""", unsafe_allow_html=True)
