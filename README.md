# 101Transfurmations

## Home App

### Models

#### Gallery Image

- The `GalleryImage` model allows the owner/admin to upload images to be used in the gallery page.
- When the images are uploaded and saved, the images are resized in order to reduce their size and help improve the loading times fo the gallery page.

## Reviews App

### Models

#### Reviews

- The `Review` model allows for customers to create a review about the company and the services that they provide.
- The `name` field has a default value of `A 101 Transfurmations Customer`, this is so that there is still a value even if the customer does not provide their name.
- The `date_added` field is automatically set when the review is saved.