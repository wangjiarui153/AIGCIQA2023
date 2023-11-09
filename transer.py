import pandas as pd
import scipy
from scipy import io

df = pd.DataFrame(columns=["name",
                           "prompt",
                           "style",
                           "class",
                           "quality_mos",
                           "authenticity_mos",
                           "correspondence_mos",
                           "quality_std",
                           "authenticity_std",
                           "correspondence_std",
                           ])
quality_mos = scipy.io.loadmat('/data/husky/ImageReward/assets/AIGCIQA2023/DATA/MOS/mosz1.mat')['MOSz'].squeeze(-1)
authenticity_mos = scipy.io.loadmat('/data/husky/ImageReward/assets/AIGCIQA2023/DATA/MOS/mosz2.mat')['MOSz'].squeeze(-1)
correspondence_mos = scipy.io.loadmat('/data/husky/ImageReward/assets/AIGCIQA2023/DATA/MOS/mosz3.mat')['MOSz'].squeeze(-1)
quality_std = scipy.io.loadmat('/data/husky/ImageReward/assets/AIGCIQA2023/DATA/STD/SD1.mat')['SD'].squeeze(-1)
authenticity_std = scipy.io.loadmat('/data/husky/ImageReward/assets/AIGCIQA2023/DATA/STD/SD2.mat')['SD'].squeeze(-1)
correspondence_std = scipy.io.loadmat('/data/husky/ImageReward/assets/AIGCIQA2023/DATA/STD/SD3.mat')['SD'].squeeze(-1)

prompt_df = pd.read_csv('/data/husky/ImageReward/assets/AIGCIQA2023/DATA/MOS/AIGCIQA2023_Prompts.csv')

for image_grp in range(0, 6):
    for prt_grp in range(0, 100):
        for id in range(0,4):
            df.loc[image_grp*400+prt_grp*4+id] = ["{}.png".format(image_grp*400+prt_grp*4+id),
                                                  prompt_df.loc[prt_grp, 'prompt'],
                                                  prompt_df.loc[prt_grp, 'style'],
                                                  prompt_df.loc[prt_grp, 'class'],
                                                  quality_mos[image_grp*400+prt_grp*4+id],
                                                  authenticity_mos[image_grp*400+prt_grp*4+id],
                                                  correspondence_mos[image_grp*400+prt_grp*4+id],
                                                  quality_std[image_grp*400+prt_grp*4+id],
                                                  authenticity_std[image_grp*400+prt_grp*4+id],
                                                  correspondence_std[image_grp*400+prt_grp*4+id],
                                                  ]

df.to_csv("/data/husky/ImageReward/assets/AIGCIQA2023/DATA/MOS/AIGCIQA2023.csv")
print(df)

