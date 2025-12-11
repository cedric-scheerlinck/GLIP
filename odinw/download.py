import argparse
import os

argparser = argparse.ArgumentParser()
argparser.add_argument(
    "--dataset_names", default="all", type=str
)  # "all" or names joined by comma
argparser.add_argument("--dataset_path", default="DATASET/odinw", type=str)
args = argparser.parse_args()

# Use /resolve/ instead of /tree/ for direct file downloads from Hugging Face
root = "https://huggingface.co/GLIPModel/GLIP/resolve/main/odinw_35"

all_datasets = [
    "AerialMaritimeDrone",
    "AmericanSignLanguageLetters",
    "Aquarium",
    "BCCD",
    "ChessPieces",
    "CottontailRabbits",
    "DroneControl",
    "EgoHands",
    "HardHatWorkers",
    "MaskWearing",
    "MountainDewCommercial",
    "NorthAmericaMushrooms",
    "OxfordPets",
    "PKLot",
    "Packages",
    "PascalVOC",
    "Raccoon",
    "ShellfishOpenImages",
    "ThermalCheetah",
    "UnoCards",
    "VehiclesOpenImages",
    "WildfireSmoke",
    "boggleBoards",
    "brackishUnderwater",
    "dice",
    "openPoetryVision",
    "pistols",
    "plantdoc",
    "pothole",
    "selfdrivingCar",
    "thermalDogsAndPeople",
    "vector",
    "websiteScreenshots",
]

datasets_to_download = []
if args.dataset_names == "all":
    datasets_to_download = all_datasets
else:
    datasets_to_download = args.dataset_names.split(",")

# Create directory if it doesn't exist
os.makedirs(args.dataset_path, exist_ok=True)

for dataset in datasets_to_download:
    if dataset in all_datasets:
        print("Downloading dataset: ", dataset)
        zip_path = os.path.join(args.dataset_path, dataset + ".zip")
        download_url = root + "/" + dataset + ".zip"

        # Download the file
        result = os.system("wget " + download_url + " -O " + zip_path)
        if result != 0:
            print(f"Failed to download {dataset}.zip")
            continue

        # Unzip the file
        result = os.system("unzip " + zip_path + " -d " + args.dataset_path)
        if result != 0:
            print(f"Failed to unzip {dataset}.zip")
            continue

        # Remove the zip file
        if os.path.exists(zip_path):
            os.remove(zip_path)
    else:
        print("Dataset not found: ", dataset)
