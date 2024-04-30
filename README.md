# Commerce

Commerce is a Django-based web application that simulates an auction site, allowing users to post auction listings, place bids, comment on listings, and add listings to a watchlist.

## Features

- **User Authentication**: Users can register, log in, and log out of the application.
- **Active Listings**: Users can view all active auction listings on the site.
- **Create Listings**: Authenticated users can create new auction listings with details such as title, description, starting bid, optional image URL, and category.
- **Place Bids**: Users can place bids on listings. The current bid is updated to reflect the highest bid placed.
- **Comments**: Users can post comments on auction listings.
- **Watchlist**: Users can add listings to their watchlist and view them separately.
- **Categories**: Users can assign categories to listings when creating them and filter listings by categories.

## Installation

To run the Commerce application locally, follow these steps:

Clone the repository:
- git clone https://github.com/lolocompa/commerce.git
- Navigate to the project directory:
- cd commerce
- Install the required dependencies:
- pip install -r requirements.txt
- Make migrations and migrate the database:
- python manage.py makemigrations
- python manage.py migrate
- Run the Django development server:
- python manage.py runserver
- Open a web browser and navigate to http://127.0.0.1:8000/ to view the application.
## Usage
- Register/Login: To create or bid on listings, you must first register for an account and log in.
- Create a Listing: Navigate to the "create listing" link in the navigation bar to create a new auction listing.
- View Listings: Click on "Active Listings" in the navigation bar to view all active listings.
- Place a Bid: On a listing's page, enter your bid amount and click "place bid" to bid on the listing.
- Add to Watchlist: Click "add to watchlist" on a listing's page to add it to your watchlist.
- View Watchlist: Click "watchlist" in the navigation bar to view all listings you've added to your watchlist.
- Comment on Listings: At the bottom of a listing's page, enter your comment and click "submit" to post a comment.
## Contributing
Contributions to the Commerce project are welcome. Please follow the standard GitHub pull request process to propose changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
