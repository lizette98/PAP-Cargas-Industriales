from wwo_hist import retrieve_hist_data
frequency = 1
start_date = "01-01-2009"
end_date = "02-21-2020"
api_key = "48236d9a55ec414e930211450201802"
#"21.1236,-101.68" leon, guanajuato
#salamanca, gto : 20.53627,-101.20445
location_list = ["New York"]
"San_Luis_Potosi"

hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)