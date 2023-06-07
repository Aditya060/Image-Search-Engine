from PIL import Image
from pathlib import Path
import numpy as np

if __name__ == "__main__":
 	for img in sorted(Path("./static/image").glob("*.jpg")):
 		print(img_path)

 		#Extracing deep feature
 		feature = fe.extract(img = Image.open(img_path))

 		feature_path = Path("./static/feature")/ (img_path.stem + ".npy")
 		print(feature_path)

 		np.save(feature_path,feature)

 		