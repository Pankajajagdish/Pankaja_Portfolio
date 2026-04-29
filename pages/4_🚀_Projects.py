import streamlit as st

st.set_page_config(page_title="Projects", page_icon="🚀", layout="wide")

st.markdown("""
<style>
    .project-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-left: 4px solid #667eea;
        padding: 25px;
        border-radius: 12px;
        margin: 20px 0;
        transition: transform 0.3s ease;
    }
    .project-title {
        font-size: 22px;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 10px;
    }
    .project-description {
        color: #64748b;
        margin: 15px 0;
        line-height: 1.6;
    }
    .project-tag {
        display: inline-block;
        background: #f0f4ff;
        color: #667eea;
        padding: 6px 12px;
        border-radius: 16px;
        margin: 5px 5px 5px 0;
        font-size: 13px;
    }
    .project-links {
        margin-top: 15px;
    }
    .project-link {
        display: inline-block;
        margin-right: 15px;
        color: #667eea;
        text-decoration: none;
        font-weight: 600;
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

st.title("🚀 Featured Projects")

projects = [
    {
        "title": "GitHub Actions CI/CD Workflows",
        "description": "Production-ready CI/CD pipelines for automated testing, building, and deploying applications to AWS and Kubernetes. Implemented matrix builds, secret management, and multi-environment deployments.",
        "technologies": ["GitHub Actions", "Docker", "AWS", "Kubernetes", "Python"],
        "impact": "Reduced deployment time by 60% and enabled 10+ daily deployments",
        "links": {
            "GitHub": "https://github.com/Pankajajagdish",
            "Blog Post": "#"
        }
    },
    {
        "title": "Kubernetes AKS Infrastructure",
        "description": "Enterprise-grade Kubernetes cluster on Azure with advanced networking, RBAC, monitoring, and auto-scaling capabilities. Implemented GitOps for infrastructure management and automated deployments.",
        "technologies": ["Kubernetes", "AKS", "Terraform", "Azure", "Helm"],
        "impact": "Managed 100+ microservices with 99.9% uptime",
        "links": {
            "Documentation": "#",
            "GitHub": "https://github.com/Pankajajagdish"
        }
    },
    {
        "title": "Multi-Cloud Monitoring Stack",
        "description": "Integrated monitoring solution with Prometheus, Grafana, and Azure Log Analytics for distributed systems observability. Created custom dashboards and alerting rules for proactive incident response.",
        "technologies": ["Prometheus", "Grafana", "Azure Monitor", "Kubernetes"],
        "impact": "Reduced MTTR (Mean Time To Resolution) by 50%",
        "links": {
            "Architecture": "#",
            "GitHub": "#"
        }
    },
    {
        "title": "Infrastructure as Code Automation",
        "description": "Complete IaC solution using Terraform for provisioning and managing cloud resources across AWS and Azure. Implemented module-based approach for reusability and best practices.",
        "technologies": ["Terraform", "CloudFormation", "Python", "Azure"],
        "impact": "Provisioned infrastructure in minutes instead of days",
        "links": {
            "Repository": "https://github.com/Pankajajagdish",
            "Documentation": "#"
        }
    },
    {
        "title": "Container Orchestration Platform",
        "description": "Advanced Kubernetes cluster management with Helm charts, service mesh integration, and automated scaling policies. Implemented blue-green deployments and canary releases.",
        "technologies": ["Kubernetes", "Helm", "Docker", "GitOps", "Istio"],
        "impact": "Enabled zero-downtime deployments",
        "links": {
            "Architecture": "#",
            "GitHub": "#"
        }
    },
    {
        "title": "Cloud Cost Optimization",
        "description": "Cost analysis and optimization framework for multi-cloud environments with automated tagging and resource management. Created dashboards for cost visibility and optimization recommendations.",
        "technologies": ["Python", "AWS", "Azure", "Cost Analysis", "Automation"],
        "impact": "Reduced monthly cloud spend by 40%",
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
        <div class="project-description">{project['description']}</div>
        <div style="margin: 15px 0;">
            <strong style="color: #667eea;">💡 Impact:</strong> {project['impact']}
        </div>
        <div style="margin: 15px 0;">
    """, unsafe_allow_html=True)
    
    for tech in project['technologies']:
        st.markdown(f'<span class="project-tag">{tech}</span>', unsafe_allow_html=True)
    
    st.markdown("""
        </div>
        <div class="project-links">
    """, unsafe_allow_html=True)
    
    for link_text, url in project['links'].items():
        st.markdown(f'[🔗 {link_text}]({url})', unsafe_allow_html=False)
        st.write("  ")
    
    st.markdown("</div></div>", unsafe_allow_html=True)

# Stats Section
st.markdown('<div class="section-title">📈 Project Statistics</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Projects", "6+")

with col2:
    st.metric("Deployments", "1000+")

with col3:
    st.metric("Uptime Achieved", "99.9%")

with col4:
    st.metric("Cost Reduction", "40%")
