import streamlit as st

# Page config
st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .main { padding-top: 0; }
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 80px 40px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 40px;
    }
    .hero-title {
        font-size: 56px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .hero-subtitle {
        font-size: 28px;
        font-weight: 500;
        opacity: 0.95;
        margin-bottom: 20px;
    }
    .hero-description {
        font-size: 18px;
        opacity: 0.9;
        max-width: 600px;
        margin: 20px auto;
    }
    .stat-card {
        background: #f0f4ff;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        border-left: 4px solid #667eea;
        margin: 15px 0;
    }
    .stat-number {
        font-size: 36px;
        font-weight: 700;
        color: #667eea;
    }
    .stat-label {
        font-size: 14px;
        color: #64748b;
        margin-top: 8px;
    }
    .cta-button {
        display: inline-block;
        background: #667eea;
        color: white;
        padding: 12px 30px;
        border-radius: 8px;
        text-decoration: none;
        margin-top: 20px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <div style="font-size: 80px; margin-bottom: 20px;">🖥️</div>
    <div class="hero-title">Hi, I'm Pankaj Jagdish</div>
    <div class="hero-subtitle">DevOps & Cloud Infrastructure Engineer</div>
    <div class="hero-description">
        AWS Certified Professional | Kubernetes Specialist | CI/CD Expert
    </div>
    <div class="hero-description">
        Building scalable cloud solutions, automating infrastructure, and optimizing deployment pipelines
    </div>
</div>
""", unsafe_allow_html=True)

# Stats Section
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">5+</div>
        <div class="stat-label">Years of DevOps Experience</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">100+</div>
        <div class="stat-label">Infrastructure Deployments</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">AWS</div>
        <div class="stat-label">Certified Professional</div>
    </div>
    """, unsafe_allow_html=True)

# Quick Overview
st.markdown("---")
st.subheader("🎯 Quick Overview")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### What I Do
    
    I specialize in designing and implementing robust **DevOps solutions** that help teams:
    - 🚀 Deploy applications faster and more reliably
    - 📊 Monitor infrastructure with comprehensive observability
    - 🔐 Maintain security and compliance standards
    - 💰 Optimize costs across multi-cloud environments
    """)

with col2:
    st.markdown("""
    ### My Expertise
    
    **Cloud & Infrastructure**
    - AWS (EC2, S3, RDS, Lambda, etc.)
    - Azure (VMs, AKS, App Services)
    - Kubernetes & Container Orchestration
    
    **Automation & CI/CD**
    - GitHub Actions, Jenkins, GitLab CI
    - Terraform, CloudFormation, Bicep
    - Docker, Helm, GitOps
    """)

st.markdown("---")

# Call to Action
st.markdown("""
<div style="text-align: center; padding: 40px; background: #f0f4ff; border-radius: 12px; margin-top: 30px;">
    <h3>Let's Work Together</h3>
    <p>Ready to transform your infrastructure? Explore my work or get in touch.</p>
</div>
""", unsafe_allow_html=True)
