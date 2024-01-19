#### Preparation of a file for SQL destination ####

# modules and libraries:
import pandas as pd

# selenium destination file location:
main_file = "\\location_path"

# default intro columns:
default_intro_columns = ['{{device_id}}',
 '{{username}}',
 '{{submitted_at}}',
 '{{received_at}}',
 '{{submission_id}}',
 '{{device_submission_identifier}}',
 '{{fields.Training_Language}}']

# default_main_columns:
default_main_columns = ['{{fields.English[0].Introduction_EN}}',
 '{{fields.English[0].Organization_EN}}',
 '{{fields.English[0].Country_of_training_EN}}',
 '{{fields.English[0].Beginning_Date_EN}}',
 '{{fields.English[0].End_Date_EN}}',
 '{{fields.English[0].Course_Name_EN}}',
 '{{fields.English[0].Learning_Mode_EN}}',
 '{{fields.English[0].The_objectives_clear_EN}}',
 '{{fields.English[0].The_learning_activities_helped_EN}}',
 '{{fields.English[0].Environment_helped_learning_EN}}',
 '{{fields.English[0].The_learning_material_helped_EN}}',
 '{{fields.English[0].Comments_EN}}',
 '{{fields.English[0].Knowledge_most_relevant_EN}}',
 '{{fields.English[0].Knowledge_least_relevant_EN}}',
 '{{fields.English[0].Level_of_expertise_before_EN}}',
 '{{fields.English[0].Level_of_expertise_after_EN}}',
 '{{fields.English[0].Knowledge_applicable_EN}}',
 '{{fields.English[0].If_below_60_reasons_EN}}',
 '{{fields.English[0].Positive_impacts_EN}}',
 '{{fields.English[0].General_Comments_EN}}']

# function to change a language:
def change_language(lang,
                    abbr,
                    lst = default_main_columns):
    
    # replace default text:
    return [x.replace("English", lang).replace("EN", abbr) for x in lst]

# function to read dm_table_id file:
def read_file():

    # read rows from 8th row:
    df = pd.read_csv(main_file,
                    header = None,
                    skiprows = 7)
    return df

# function to transform lists
# and to save and overwrite main file:
def transform_and_save():

    # transform:                                               # change full language and abbr:
    final = [x + y for x,y in zip((read_file()[0].to_list()), (change_language("French", "FR")))]
    
    # concat intro and transformed lists into one:
    dataframe = default_intro_columns + final

    # save and overwrite file:
    final_df = pd.DataFrame(dataframe)
    final_df.to_csv(main_file,
                    header = None,
                    index = None,
                    mode = "w")
    print("Destination file has been overwriten!")