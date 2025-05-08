# Palestine Courses Group (PCG)
#### Video Demo:  <URL https://drive.google.com/file/d/1HqWJ7IqSnAqGWn_3N6iAPklUi6ncFjH0/view?usp=sharing>
#### Description:

Description

Palestine Courses Group (PCG) is a web-based platform built with Flask that serves as a comprehensive and centralized hub for academic and vocational learning spaces across Palestinian cities. The platform aims to provide users—especially students and freelancers—with up-to-date, filtered information about co-working spaces, study hubs, and educational centers available in their area.

The site is fully localized in Arabic with RTL (right-to-left) design and features a clean, responsive, and user-friendly interface. It allows users to browse available learning spaces, filter them by city, and view essential details such as location, services offered, working hours, contact information, and more. A search filter is implemented for more efficient navigation and better user experience.

Project Files
app.py
The main backend file built with Flask. It handles routing, data logic, and the filtering mechanism based on user-selected cities.

templates/homepage.html
The landing page of the platform. It includes a welcome message, introduces the purpose of the platform, and provides navigation links to other pages.

templates/courses.html
Displays all available learning spaces using styled cards. Each card contains an image, name, location, list of features, and contact details.

templates/about.html
An informational page outlining the mission of PCG and its commitment to promoting accessible educational environments.

static/css/styles.css
Custom CSS file for all visual styling. It includes support for RTL layout, grid structure, card designs, typography, hover effects, and responsive behavior.

static/images/
A folder containing logos and representative images for each listed space.

Technologies Used
Python 3 – Core programming language used to build the backend.

Flask – Lightweight web framework used for routing, templating, and application logic.

HTML5 – For structuring the frontend pages and content.

CSS3 – For custom styling, layout, RTL support, and responsiveness.

Jinja2 – Templating engine used to dynamically render HTML content.

Bootstrap (optional) – Used selectively to aid in responsive design (if applied).

VS Code – Main development environment.

Git – Version control system used for managing the project.

GitHub – Hosting platform for the project repository and version tracking.

Design Choices
Flask Framework
Chosen for its simplicity, flexibility, and suitability for small to mid-sized projects. Flask enabled rapid development and clean routing logic.

RTL and Arabic Language Support
Since the platform targets Palestinian users, full RTL support and Arabic typography were essential for accessibility and ease of reading.

Card-Based UI
A card layout was selected to clearly display individual learning spaces. This enhances readability and is more responsive across different screen sizes.

Filtering Feature
A city-based filter is positioned at the top of the page to enable users to quickly narrow down results without unnecessary scrolling.

Modular Design
Separation of templates and CSS allows for future scalability. The structure supports potential additions such as login functionality or an admin dashboard.

Challenges and Considerations
Several key UI/UX decisions were made during development. Initially, the city filter was placed on the side, but based on usability feedback, it was repositioned at the top for better visibility and flow. The design of the cards was refined to strike a balance between visual simplicity and informational completeness.

Mobile responsiveness posed particular challenges with Arabic text alignment and spacing. Extra care was taken to adjust padding, fonts, and grid layouts to ensure a consistent experience across all devices.


Future Improvements
Add user registration and login functionality to allow saving or reviewing favorite spaces.

Implement a dynamic database (e.g., SQLite or PostgreSQL) for managing listings.

Integrate interactive maps to visualize space locations by city.

Develop an admin panel for reviewing and approving submitted listings.

Conclusion
Palestine Courses Group (PCG) is designed to be accessible, lightweight, and tailored to local needs. It empowers Palestinian learners by making it easier to discover the best environments for productivity, creativity, and growth. The current version lays a strong foundation that can evolve to include features like real-time availability, user reviews, and regional partnerships.