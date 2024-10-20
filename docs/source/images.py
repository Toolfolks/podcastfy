# Generate podcast from input images
image_paths = [
	"./data/images/Senecio.jpeg",
	"./data/images/connection.jpg"
]

audio_file_from_images = generate_podcast(image_paths=image_paths)

print("Podcast generated from images:", audio_file_from_images)