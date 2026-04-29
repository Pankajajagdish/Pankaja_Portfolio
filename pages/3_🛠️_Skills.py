import streamlit as st

st.set_page_config(page_title="Skills", page_icon="🛠️", layout="wide")

st.markdown("""
<style>
    .skill-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 25px;
        border-radius: 12px;
        margin: 10px 0;
    }
    .skill-category {
        background: #f0f4ff;
        padding: 20px;
        border-radius: 12px;
        margin: 20px 0;
    }
    .skill-tag {
        display: inline-block;
        background: #667eea;
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        margin: 5px;
        font-size: 14px;
    }
    .progress-container {
        background: #f0f4ff;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
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

st.title("🛠️ Technical Skills")

# Cloud & Infrastructure
st.markdown('<div class="section-title">☁️ Cloud & Infrastructure</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="skill-category">
        <h4>AWS</h4>
        <p>EC2, RDS, S3, Lambda, CloudFormation, IAM, VPC, ALB, Auto Scaling, CloudWatch</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="skill-category">
        <h4>Azure</h4>
        <p>Virtual Machines, App Services, AKS, SQL Database, Cosmos DB, Azure DevOps, Bicep</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="skill-category">
        <h4>Kubernetes</h4>
        <p>K8s Architecture, Deployments, StatefulSets, DaemonSets, Services, Ingress, RBAC, Helm</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="skill-category">
        <h4>Container Tech</h4>
        <p>Docker, Docker Compose, Container Registry, Image Optimization, Security Scanning</p>
    </div>
    """, unsafe_allow_html=True)

# CI/CD & Automation
st.markdown('<div class="section-title">🔄 CI/CD & Automation</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="skill-category">
        <h4>GitHub Actions</h4>
        <p>Workflows, Actions, Matrix Builds, Deployment Strategies, Secrets Management</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="skill-category">
        <h4>Jenkins</h4>
        <p>Pipelines, Declarative/Scripted, Plugins, Distributed Builds, Integration</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="skill-category">
        <h4>Infrastructure as Code</h4>
        <p>Terraform, CloudFormation, Ansible, Bicep, GitOps</p>
    </div>
    """, unsafe_allow_html=True)

# Monitoring & Logging
st.markdown('<div class="section-title">📊 Monitoring & Logging</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="skill-category">
        <h4>Prometheus & Grafana</h4>
        <p>Metrics Collection, Alerting, Dashboard Creation, PromQL, Time-Series Data</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="skill-category">
        <h4>ELK Stack</h4>
        <p>Elasticsearch, Logstash, Kibana, Log Aggregation, Analysis</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="skill-category">
        <h4>Cloud Native Monitoring</h4>
        <p>Azure Monitor, CloudWatch, Datadog, New Relic</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="skill-category">
        <h4>Observability</h4>
        <p>Distributed Tracing, Application Insights, Logging Strategies</p>
    </div>
    """, unsafe_allow_html=True)

# Programming Languages
st.markdown('<div class="section-title">🐍 Programming Languages</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

languages = {
    "Python": 90,
    "Bash": 85,
    "JavaScript": 75,
    "Go": 70
}

for idx, (lang, proficiency) in enumerate(languages.items()):
    with [col1, col2, col3, col4][idx]:
        st.markdown(f"""
        <div class="progress-container">
            <h4>{lang}</h4>
            <div style="background: #e2e8f0; border-radius: 10px; height: 10px; overflow: hidden;">
                <div style="background: linear-gradient(90deg, #667eea, #764ba2); width: {proficiency}%; height: 100%; border-radius: 10px;"></div>
            </div>
            <p style="text-align: center; margin-top: 8px; font-size: 12px; color: #64748b;">{proficiency}%</p>
        </div>
        """, unsafe_allow_html=True)

# Additional Skills
st.markdown('<div class="section-title">⚙️ Additional Skills</div>', unsafe_allow_html=True)

additional_skills = {
    "DevOps Practices": ["Infrastructure Automation", "Configuration Management", "Deployment Strategies", "Disaster Recovery"],
    "Security": ["IAM", "RBAC", "Secret Management", "Container Security", "Compliance"],
    "Development Tools": ["Git", "GitHub", "GitLab", "JIRA", "Confluence"],
    "Databases": ["PostgreSQL", "MySQL", "MongoDB", "DynamoDB", "Redis"]
}

for category, skills in additional_skills.items():
    st.markdown(f"**{category}**")
    skill_html = " ".join([f'<span class="skill-tag">{skill}</span>' for skill in skills])
    st.markdown(f'<div>{skill_html}</div>', unsafe_allow_html=True)
    st.markdown("")
