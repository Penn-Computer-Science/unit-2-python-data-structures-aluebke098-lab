import pandas as pd

bNames = ["Noah", "Liam", "Jacob", "William", "Mason", "Ethan", "Michael", "Alexander", "James", "Elijah"]
gNames = ["Emma", "Olivia", "Sophia", "Isabella", "Ava", "Mia", "Abigail", "Emily", "Charlotte", "Madison"]

bFreq = [183330, 173981, 163266, 159945, 157875, 149082, 145171, 142142, 139652, 137093]
gFreq = [195028, 184528, 181132, 170559, 155844, 129088, 118713, 117626, 102470, 98419]

df = pd.DataFrame(
    {
        'Boys_Names':bNames,
        'B_Freq':bFreq, 
        'Girls_Names':gNames,
        'G_Freq':gFreq
    }
)

print(df)
print(round(df.describe()))