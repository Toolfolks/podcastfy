from podcastfy.client import generate_podcast

custom_config = {
    "word_count": 6000,
    "conversation_style": ["casual", "humorous"],
    "podcast_name": "Steve Warbys Info Podcast",
    "creativity": 0.7
    
    }



generate_podcast(
    urls=["https://wilsea.com/dementiaChat3/the_dementia_guide.txt"],
    #urls =["https://www.dewalt.co.uk/products/storage","https://www.dewalt.co.uk/products/storage/backpacks","https://www.dewalt.co.uk/products/storage/mobile-tool-storage","https://www.dewalt.co.uk/products/storage/storage-combo-kits","https://www.dewalt.co.uk/products/storage/tool-bags-pouches-belts","https://www.dewalt.co.uk/products/storage/tool-organizers-bins","https://www.dewalt.co.uk/products/storage/trolleys","https://www.dewalt.co.uk/products/storage/workshop-storage"],
    
    
    conversation_config=custom_config,
    tts_model="openai"
)

#audio_file_from_pdf = generate_podcast(urls=["./data/pdf/s41598-024-58826-w.pdf"])
#https://github.com/souzatharsis/podcastfy/blob/main/usage/conversation_custom.md