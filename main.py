import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import OrderedDict
from faker import Faker
from IPython.display import display

fake = Faker()

# Personal Information
personal_info = OrderedDict({
    'Name': fake.name(),
    'Title': "Marketing Data Analyst",
    'Location': fake.address(),
    'Phone': fake.phone_number(),
    'Email': fake.email(),
    'LinkedIn': f"www.linkedin.com/in/{fake.user_name()}/",
    'Languages': ['English', 'Hebrew']
})

# Career Summary
career_summary = '''
Experienced and team-focused data analyst with a background in online advertising. With 10
years of industry experience, I have managed large-scale campaigns and high-value assets,
resulting in significant yearly revenue for the company. Skilled in data analysis and online
marketing, I have a proven track record of utilizing data to make informed business decisions
and achieve goals. Analyze large scale of data sets and sources in order to optimize and improve
business KPI’s in both B2B SaaS and B2C companies.
'''

# Work Experience
work_experience = pd.DataFrame({
    'Company': [fake.company(), fake.company(), fake.company(), fake.company()],
    'Position': ['Marketing Data Analyst & Amazon Account Manager', 'Catalog Manager & Data Analyst', 'Head of Supply & Operations Team Leader', 'Product Manager'],
    'Period': ['2021-Present', '2018-2021', '2017-2018', '2014-2017'],
    'Key_Projects': [
        'Inventory optimization, Sales forecasting',
        'Daily reports & dashboards, Fulfillment strategy',
        'Supply chain reporting, Market analysis',
        'Programmatic buying strategies, Market segmentation'],
    'Tools_Technologies': [
        'Excel, SQL, Looker',
        'Django, Power BI, Qlik Sense',
        'Tableau, Excel',
        'OpenX, Google Ad Manager, PubMatic, Magnite, PulsePoint, Adform'],
    'Description': [
        '''
        Utilized advanced data analysis techniques to optimize product listings, prices and
        inventory levels, resulting in a 20% increase in sales YoY.
        Developed and implemented a dynamic inventory and sales dashboard using Excel, SQL &
        Looker to improving overall efficiency and transparency.
        Collaborated with cross-functional teams to resolve complex account health issues,
        ensuring compliance with Amazon's legal and technical requirements.
        Produced sales forecasting reports and presented insights to senior leadership, leading to
        the creation of new product offerings and market expansion.
        ''',
        '''
        Managed a catalog of over 300K products across 6 Amazon marketplaces, Walmart, and
        Shopify, Using Django and In-House app, ensuring accurate product information.
        Developed daily reports and dashboards for Ecommerce using data analytics platforms like
        Power BI and Qlik Sense to drive growth through business insights
        Successfully solved legal and technical issues with Amazon, maintaining compliance and
        preserving the company's reputation.
        Led the company's fulfillment by Amazon strategy, balancing inventory and maximizing
        profitability through effective demand and supply management.
        ''',
        '''
        Managed over 50 supply partners and fostered long-term relationships to ensure
        successful cooperation while measuring and analyzing each partner to reach maximum
        potential of video ads.
        Utilized data insights to collaborate with algorithm developers and improve product
        quality.
        Conducted market analysis to inform supply chain decisions and optimize resource
        allocation.     Designed and implemented reporting systems using business intelligence tools such as
    Tableau to drive informed decision making and drive process improvements in the supply
    chain operations.
    Managed and analyzed large sets of supply chain data to identify trends, inefficiencies, and
    opportunities for improvement.
    Communicated effectively with cross-functional teams to coordinate and streamline
    operations, ensuring seamless and efficient supply chain processes.
    ''',
    '''
    Managed video ads across 150 direct publishers to increase profits and drive ROI. working
    on several SSPs \ DSPs including: OpenX, Google Ad Manager, PubMatic, Magnite,
    PulsePoint, Adform and more.
    Analyzed campaign data and leveraged insights to inform and optimize programmatic
    buying strategies.
    Utilized real-time bidding platforms to manage and execute efficient, data-driven
    advertising campaigns.
    Collaborated with advertisers worldwide to maximize the impact of ongoing campaigns
    and identify new opportunities.
    Conducted market analysis and segmentation using Excel & Google Sheets to improve ad
    performance.
    Effectively communicated campaign performance, insights, and recommendations to
    stakeholders to drive growth and business success.
    '''
]
})
# Education
education = pd.DataFrame({
    'Degree': ['Bachelor of Arts in Mass Communication'],
    'Major': ['Digital, specializing in Project Management, Market Analysis, Account Management, Internet Marketing, SEO, New Media, Web Development, PHP, Drupal, Joomla, Photoshop, and Statistics'],
    'Institution': [f'The {fake.job()} University'],
    'Period': ['2008-2011']
})

#Skills
skills = pd.Series([
'Strong analytical and problem-solving skills',
'Proficiency in data visualization and presentation tools such as Looker Studio & Power BI',
'Experience with HTML, JS, Python, SQL and Big data repositories',
'CMS experience: Wordpress, WooCommerce, Shopify, Joomla & PrestaShop',
'Excellent communication and collaboration skills',
'Ability to work with large and complex datasets',
'Ability to translate business requirements into technical solutions',
'Strong understanding of data cleaning and preprocessing techniques'
])

#Awards & Certifications
awards_certifications = pd.Series([
'Google Analytics Individual Qualification',
'Tableau Desktop Specialist Certification',
'Python for Data Science and Machine Learning Bootcamp'
])

# Display Data
print(f"PERSONAL INFORMATION:\n")
for key, value in personal_info.items():
    print(f"{key}: {value}")
    print("\nCAREER SUMMARY:")
    print(career_summary)
    print("\nWORK EXPERIENCE:")
    display(work_experience)
    print("\nEDUCATION:")
    display(education)
    print("\nSKILLS:")
    print(skills.to_string(index=False))
    print("\nAWARDS & CERTIFICATIONS:")
    print(awards_certifications.to_string(index=False))
