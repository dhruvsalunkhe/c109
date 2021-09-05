import pandas as pd
import statistics
import csv

df = pd.read_csv("data.csv")
heightlist = df["Height"].tolist()
weightlist = df["Weight"].tolist()

heightmean = statistics.mean(heightlist)
weightmean = statistics.mean(weightlist)
heightmode = statistics.mode(heightlist)
weightmode = statistics.mode(weightlist)
heightmedian = statistics.median(heightlist)
weightmedian = statistics.median(weightlist)

print("mean,median,mode of height is {},{},and {} respectively".format(heightmean,heightmedian,heightmode))
print("mean,median,mode of weight is {},{},and {} respectively".format(weightmean,weightmedian,weightmode))

sd_height= statistics.stdev(heightlist)
sd_weight= statistics.stdev(weightlist)

height_first_sd_start,height_first_sd_end = heightmean-sd_height,heightmean+sd_height

height_second_sd_start,height_second_sd_end = heightmean-(2*sd_height),heightmean+(2*sd_height)

height_third_sd_start,height_third_sd_end = heightmean-(3*sd_height),heightmean+(3*sd_height)

heightlist_data_within_1_sd = [result for result in heightlist if result > height_first_sd_start and result < height_first_sd_end]

heightlist_data_within_2_sd = [result for result in heightlist if result > height_second_sd_start and result < height_second_sd_end]

heightlist_data_within_3_sd = [result for result in heightlist if result > height_third_sd_start and result < height_third_sd_end]

print("{}% of data for height lies within 1 sd range".format(len(heightlist_data_within_1_sd)/len(heightlist)*100))

print("{}% of data for height lies within 2 sd range".format(len(heightlist_data_within_2_sd)/len(heightlist)*100))

print("{}% of data for height lies within 3 sd range".format(len(heightlist_data_within_3_sd)/len(heightlist)*100))

weight_first_sd_start,weight_first_sd_end = weightmean-sd_weight,weightmean+sd_weight

weight_second_sd_start,weight_second_sd_end = weightmean-(2*sd_weight),weightmean+(2*sd_weight)

weight_third_sd_start,weight_third_sd_end = weightmean-(3*sd_weight),weightmean+(3*sd_weight)

weightlist_data_within_1_sd = [result for result in weightlist if result > weight_first_sd_start and result < weight_first_sd_end]

weightlist_data_within_2_sd = [result for result in weightlist if result > weight_second_sd_start and result < weight_second_sd_end]

weightlist_data_within_3_sd = [result for result in weightlist if result > weight_third_sd_start and result < weight_third_sd_end]

print("{}% of data for weight lies within 1 sd range".format(len(weightlist_data_within_1_sd)/len(weightlist)*100))

print("{}% of data for weight lies within 2 sd range".format(len(weightlist_data_within_2_sd)/len(weightlist)*100))

print("{}% of data for weight lies within 3 sd range".format(len(weightlist_data_within_3_sd)/len(weightlist)*100))




