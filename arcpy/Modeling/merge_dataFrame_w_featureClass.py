# Spatial Join

def merge_dataFrame_w_featureClass(df, fc_name, 
                                   new_name,
                                   left_on,
                                   right_on,
                                  field_types):
    
    '''df should be a pandas dataframe
    fc_name should be a string referring to a feature class in your GDB
    new_name should be a string for the new feature class
    left_on should be the field to merge from on the featureClass
    right_on should be the column to merge from the dataframe
    field_types should be a list of ESRI field types - 
    see https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/add-fields.htm'''
    
    import arcpy
    
     # Get the feature class fields

    field_names = []
    fields = arcpy.ListFields(fc_name)
    for field in fields:
        field_names.append(field.name)

    # Get the dataframe columns

    new_fields = list(df.columns)

    # Rename any repeat field names

    for field_name in list(set(new_fields) & set(field_names)):

        new_fields = [field_name + '_df' if item == field_name else item for item in new_fields]

    
    # Initialize New Feature Class
    
    if new_name in arcpy.ListFeatureClasses():
        
        print('ERROR: Please delete or rename the feature class', new_name)

    else:
        
        field_desc = list(zip(new_fields, field_types))
        
        arcpy.management.CopyFeatures(fc_name, new_name)

        arcpy.management.AddFields(new_name, field_desc)
        
        with arcpy.da.UpdateCursor(new_name, [left_on] + new_fields) as cursor:
    
            for row in cursor:

                df_row = df[df[right_on] == row[0]]

                if len(df_row) == 0:
                    pass
    #                 print('error on', row[0])

                else: # Add to the merge
                    row[1:] = list(df_row.iloc[0])

                    cursor.updateRow(row)