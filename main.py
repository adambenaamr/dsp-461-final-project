import kagglehub

# Download latest version
dataset = kagglehub.competition_download('rsna-knee-abnormality-detection')

print(f'Path to competition files: {dataset}')
