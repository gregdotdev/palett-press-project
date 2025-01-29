# Palette Press News Website

This is a simple news website built with Flask. The website showcases the latest news updates, allowing users to browse through a list of articles and view detailed content on each one. It also features a subscription form for a newsletter.

## Features

- **Homepage**: Displays the latest news articles.
- **News Detail Page**: Displays detailed content for each news article when selected.
- **Newsletter Subscription**: Allows users to subscribe to updates.
- **Responsive Design**: Optimised for both desktop and mobile views.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Flask

You can install Flask using pip if it is not already installed:

```bash
pip install flask
```

## Project Structure

```plaintext
/PalettePress
│
├── app.py                # The main Flask application
├── templates/
│   ├── index.html        # The homepage template
│   └── news_details.html # The news detail page template
└── static/
    └── style.css         # The CSS for styling the pages
```

## Running the Application

1. Clone this repository to your local machine.
   
2. Navigate to the project folder:

   ```bash
   cd PalettePress
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Open a web browser and go to `http://127.0.0.1:5000/` to view the website.

## Application Overview

- **app.py**: This is the main Python file that contains the Flask application and routes. It defines the news data and handles requests to show news articles and individual article details.

- **index.html**: The homepage of the site, which includes a list of the latest news items. It fetches the news data from the Flask app and displays each news article title, short content, and image.

- **news_details.html**: A page that displays the detailed content of a specific news article. When a user clicks on a news item from the homepage, they are redirected to this page to see the full content.

- **style.css**: Contains the styles for the website, including layout, colours, and animations.

## Sample Data

The site uses a list of sample news data, which includes:

- **Title**: The headline of the news article.
- **Content**: A brief overview of the article.
- **Image URL**: The image related to the news item.

You can add or modify news items in the `news_data` list in the `app.py` file.

## Example of News Data Format

```python
news_data = [
    {
        "title": "Varios Famous People around the music world arrived to london!",
        "content": "Various famous people arrived to London...",
        "image_url": "https://example.com/image1.jpg"
    },
    {
        "title": "US Artists arrived to London",
        "content": "In faucibus metus ac hendrerit dignissim...",
        "image_url": "https://example.com/image2.jpg"
    }
]
```

## Technologies Used

- **Flask**: A lightweight web framework for Python.
- **HTML/CSS**: Used for the structure and styling of the site.
- **Jinja2**: Templating engine used to render dynamic content on HTML pages.

## License

This project is open-source and available under the MIT License. Feel free to modify and use it as needed.

---

If you encounter any issues or have questions, feel free to open an issue in the repository.
