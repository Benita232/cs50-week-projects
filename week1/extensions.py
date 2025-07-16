

    # Prompt user for filename and clean input
filename = input("File name: ").strip().lower()
# Dictionary mapping file extensions to MIME types
mime_types = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

    
    # Extract extension (portion after last dot)
if '.' in filename:
        extension = filename.split('.')[-1]
        print(mime_types.get(extension, "application/octet-stream"))
    # If no extension, default to application/octet-stream
else:
        print("application/octet-stream")
    # Output MIME type or default if unknown
    