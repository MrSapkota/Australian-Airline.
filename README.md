# Australian-Airline.
                                                                                                         Virgin Australia Performance Analysis Report

                              
1. Abstract
I combed through the data to extract and enrich these insights and produced several visualizations on how Virgin Australia is performing across its flights. Using Tableau and Python, my goal is to find trends and patterns, and drill for opportunities. With my analysis we find large differences in punctuality, capturing how cancellations and operational disturbances tend to occur for many routes. I provide insight into Virgin Australia operations on how to increase operational efficiency, customer satisfaction through interactive dashboards and detailed visualizations.
 2. Introduction
It keeps things running on time-to take off from around the country and to land on any one site without delay. The introduction to Virgin Australia's flight performance I use powerful visualization tools such as Tableau and Python to turn complex figures into simple insights in this report. By examining trends, identifying patterns, and pin-pointing areas of improvement, I hope to contribute to the improvement of Virgin Australia's service reliability. By a series of visualizations, I aim to give a detailed analysis in summary form that presents the airline highlights, along with pertinent findings and proposals.
 3. Visualization Software
 Tableau's user-friendly design allows for a seemingly complex dataset to be shown in handier visualizations that are far easier than anything we had before. This means that Tableau is the perfect tool for people with real data problems: using it I explored my data from many different angles; looked at trends in the spark lines of the data set and made truly data-driven decisions. Its advanced functions mean that i can not only draw a simple bar chart but also use it as an essential tool for statistical analyses and modeling. (Tableau Software. (2024). "Tableau Dashboard and Story Creation." Retrieved from Tableau Documentation) (Jahns, 2014)
Python: For data analysis and display, Python has developed into a powerful programming language. Thanks to tools like Pandas for manipulating data, Matplotlib for plotting and Seaborn to generate super stats graphs in Python it easier than ever before to clean, analyze the results of an experiment, and display them to others in a clear format for their benefit or scrutiny. Especially handling huge datasets and performing complicated calculations, it is very useful now. (Pajankar, 2021)
4. Graphical Visualization Techniques
4.1.	 Heat Map: Color shade represents the values; High and Low performance areas will be easily traceable in this diagram. It is particularly suitable for recognizing patterns and trends from large amounts of data along with multiple dimensions of data.  (Wilkinson & Friendly, 2009)
4.2.	Scatter Plot: Positive correlations generally long for larger scatter, while the opposite is true for negative ones called regression scatters. A scatter plot is composed of numerous location points-the x, y of each point equals one pair data variables. Determining which way of causality exists before proceeding with analysis (or indeed any kind) is important! Then we can confirm or revise any earlier speculation based on those correlations using directed graphs: this will make it easier for readers to understand what was already received and what needs not be reviewed again Scatter plots show how two sets of data compare to each other. (Keim et al., 2009)
4.3.	Geo-visualization: Geo-visualizations display the distribution of flight performance through data on map. This was to understand how EACH location effects on time departures and arrivals and identifying regions and hotspots. (Feibush et al., 1999)
4.4	Dual Axis Chart: With this chart I plotted two different variables onto the same graph, each with its y-axis. An example includes plotting the number of scheduled flights against cancellations over time obtaining a more holistic perspective on the information. (Isenberg et al., 2011)
4.5.	Time Trend: Line Graph Time trend graphs depict a specific metric across time. These are necessary to know, however, to get the full picture of how the overall flight is performing over a longer period or through seasonal factors. 
4.6.	Bar Graph: Bar graphs are ideal to compare the categories. I used them to plot the average on-time arrival percentage for various routes, showing clearly which routes to do well, and which routes to need a boost. (Quach & Jenny, 2020)
 5. Data Overview
The data I used to analyze extends over many performance metrics for Virgin Australia flights, enabling a complete picture of their operations. The dataset consists of:
•	Routes: Details of the individual flight routes, illustrating where the feed is flying in/out of. 
•	Departing and Arriving Ports: Details about the airports from which flights depart and to which planes arrive, helping to add a sense of geography.
•	Years: The time series data is over years and on the right, it is spread over months, allowing us to have more look at trends over time
•	Sectors Scheduled and Flown: This shows the Number of Flights Planned Against No. of Flights Operated, which gives us information on the operations compliance of the day.
•	Cancellations: The number of flights that were cancelled, which offers some insight as to where the issues are. 
•	On-Time Departures and Arrivals: The flights that left the departure city and arrived at the destination.
•	Geographical Coordinates: Visualizations Geographical Coordinates (Lat & Long from departing port and arriving) so that we can further drill down to geographical level
6. Visualization and Analysis
In this section, I delve into the visualizations created to analyze Virgin Australia's flight performance. Each visualization provides unique insights and helps us understand different aspects of the data. 

6.1 Geographical Distribution of On-Time Departures

![image](https://github.com/user-attachments/assets/d36a1314-0169-44bc-9d81-f30bc7aa47f6)

                                                                                            
                                                                       Fig: 1
                                      ![image](https://github.com/user-attachments/assets/bce08e6d-626a-4d3d-9714-20e51ef95ab9)
                                                
                                                                      Fig:1.1
On-Time Departure percentage across Virgin Australia's routes for the Geographical Distribution of On-Time Departures visualization (Fig:1) Green means on-time performance is high, while red suggests lower on-time performance. The map might subsequently look like this, which provides immediate visualization of which routes are doing great and which need help.
The tooltip features the specific on-time departure rate, and each route is, of course, captioned with their respective departure and arrival airports. This interactive map allows operational managers the ability to recognize trends and trouble-spots and can quickly respond with targeted changes to improve overall on-time performance and customer satisfaction.
6.2. Yearly Trends in Sectors Scheduled and Cancellations
 ![image](https://github.com/user-attachments/assets/d6f7d01d-42ef-441a-a1a3-538813a02790)
                                                                                       
                                                                       Fig: 2
 ![image](https://github.com/user-attachments/assets/f9847b36-05e2-418a-8fef-fcf9d8db2aa0)

       Fig:2.1
(Fig 2 ) Yearly Trends in Sectors Scheduled and Cancellations Virgin Australia This compares changes and trends, indicating high periods of cancellations and possible operational problems. The x-axis represents the years represented, and the y-axis indicates the number of sectors scheduled and cancellations. Going through the chart top to bottom gives you another way to view how much scheduling practices and exogenous factors influence the number of cancellations on a year-by-year basis by hovering over the data. The resultants of this visualization are applied to find critical times for actions and the strategies to reduce cancellation and improve dependability.



6.3. Trend of On-Time Departures Over Time
![image](https://github.com/user-attachments/assets/a8023d10-e07c-4692-bdba-dcde1dcbcbec)
                                                                                        
Fig: 3
 ![image](https://github.com/user-attachments/assets/567eb6b8-4ab6-439a-81b3-edd3d3330f17)

       Fig: 3.1
The Trend of On-Time Departures Over Time visualization (Figure 3) provides insight about on-time departure of Virgin Australia flights over multiple years. This chart is a line chart to represent whether the percentage of departures on time has increased or decreased in the period being analyzed. Years are being plotted on the x-axis, % on-time departures on the y-axis. The chart allows Hover-over to see the exact percentages for each year, giving very clear insights into performance trends. This visualization is useful because it allows us to see the trends; better or worse periods of on-time performance, and to see which parts of the flights are on time or delayed.
6.4. Average On-Time Arrivals by Route
  ![image](https://github.com/user-attachments/assets/23bdc952-f35b-420d-8fef-19f67723e06b)

                                                                         Fig: 4
 ![image](https://github.com/user-attachments/assets/9fd98161-5725-4049-bd3b-5ee2cb14329d)

Fig: 4.1
Average On-Time Arrivals by Route the Average On-Time Arrivals by Route visualization (Fig: 4) shows you how well Virgin Australia flights keep to time on each route. Bar Chart: Breakdowns of Best and Worst Routes in % of Arrivals on Time Each bar shows a route (departure and arrival airports) When a user navigates over a bar, the average on-time arrival percentage (precise to a single digit) displays, allowing a person to quickly refer to which routes are doing well and which need work. This can track the routes that are doing very well and can lay more focus on the routes that are not making the desired profit and need an operational upgrade.
 6.5. Variation in On-Time Arrivals by Route 
 ![image](https://github.com/user-attachments/assets/c5d9f1c5-7c22-4d86-87ee-db6a048baacb)
                                                                                   
Fig: 5
 ![image](https://github.com/user-attachments/assets/c1de36da-f719-4ce9-a9de-4d77e42c1e6b)
                                                                                
Fig: 5.1
(Fig: 5) On-Time Arrivals by Route and Year Changes by Route and Month Representation of the variation in on-time performance across routes and months Heat map of on-time arrivals across the year Heat maps depict monthly variations that the colors can show peaks and troughs with respect to schedule arrival slots and resulting in potential seasonal challenges on the route. A route-month combination that provides the on-time percentages for each cell when you hover over them. It highlights the exact time and routes for which operational improvements are needed.
6.6. Relationship Between Sectors Scheduled and Cancellations
     ![image](https://github.com/user-attachments/assets/d5da011c-815d-4f46-918a-c3b49cdfce8c)
           
     Fig: 6
     ![image](https://github.com/user-attachments/assets/2bdc375e-2f96-46ca-ad5c-ad057da646b3)
                                                                                   
Fig: 6.1
  The number of scheduled flights affecting the departure cancellations has been visualized in the figure below depicting the relationship between Sectors Scheduled and Cancellations (Fig: 6). A scatter plot with trend lines is being presented with Every route represented as a point where Simply schedules result sometimes in increased cancellations. Hover the pointer over a point to display the number of scheduled flights and cancellations in the system. The Visualization: helps to quickly identify problem areas in the GIS for topographic path routes which may result in higher driver shuffles by which drivers can be guided to enhanced planning and reduced cancel drives.
 7. Dashboard and Story 
7.1 Dashboard
   ![image](https://github.com/user-attachments/assets/25bc9f12-3c1b-4fd1-98ef-a6e27357ff72)
                                                                                               
Fig: 7
Virgin Australia Performance Dashboard. Virgin Australia Performance Dashboard (Fig: 7) provides a top-level view of the most important visualizations to give a full picture of where the airline stands. The dashboard is highly interactive, allowing users to filter data by route, and month to enable detailed exploration of individual trends or challenges. It funnels data in increasingly fine granularity for separate applications that require such a hierarchy, and data flows through the system as well (e.g., between development, testing and production environments) 
7.2. Story
Virgin Australia Performance Story explains all the visualizations and lets the viewers get through the analysis. This information provides an overall view of how the airline is performing in terms of the percentage of on-time departures, the distribution of on-time departure geographically, in terms of trends over the years in sectors scheduled and cancellations, over a period of time in on-time departures, on an average of on-time arrivals by route, variations of on-time arrivals by route and month and a relationship between sectors scheduled and cancellations. This story-based organization of data enables viewers to grasp the results and recommendations, thus rendering the data useful and meaningful.
     7.2.1. Overview of Virgin Australia's Performance
                                                                                          
![image](https://github.com/user-attachments/assets/9c4d48b2-300d-464b-9068-bf0f2e5f402c)

                                                               Fig: 8
   
7.2.2. Geographical Distribution of On-Time Departures
 ![image](https://github.com/user-attachments/assets/984702de-a1e4-436e-a966-7a9625d74e2e)

         Fig : 9    
 7.2.3. Yearly Trends in Sectors Scheduled and Cancellations
 ![image](https://github.com/user-attachments/assets/70f8383b-2f69-4a1c-8cb0-789610873b69)

         Fig: 10
  7.2.4. Trend of On-Time Departures Over Time
       
  ![image](https://github.com/user-attachments/assets/2acde502-4f40-41da-821e-8a6615b6f9c8)

    Fig: 11

  7.2.5. Variation in On-Time Arrivals by Route and Month
 ![image](https://github.com/user-attachments/assets/2772abad-718b-46f4-ac94-0109fde56615)

                  Fig: 12

7.2.6. Relationship Between Sectors Scheduled and Cancellations
 ![image](https://github.com/user-attachments/assets/3e36cfac-f3b7-4e9a-8ea4-c1b2b41ec8fd)

     Fig: 13
7.2.7. Summary and Recommendations
![image](https://github.com/user-attachments/assets/a8ad129d-efa8-4de9-a437-a55efd200ec0)

                                                                         Fig: 14
8. Summary and Recommendations
 8.1. Summary:
Virgin Australia Performance Story-explains all the visualizations and let the viewers to get through the analysis. This information provides an overall view of how the airline is performing in terms of the percentage of on-time departures, the distribution of on-time departure geographically, in terms of trends over the years in sectors scheduled and cancellations, over a period of time in on-time departures, on an average of on-time arrivals by route, variations of on-time arrivals by route and month and a relationship between sectors scheduled and cancellations. This story-based organization of data enables viewers to grasp the results and recommendations, thus rendering the data useful and meaningful. 
8.2. Recommendations: 
8.2.1. Focus on Routes with High Cancellation Rates: 
o	Target strategies to raise cancellations on routes such as Sydney to Melbourne. 
o	What's the real reason for these cancellations? Could it be maintenance shortfalls and independent disturbances? Find out. And do something about it. 
8.2.2. Improve On-Time Performance: 
o	Improve the scheduling, communication and maintenance procedures. 
o	Regularly monitor performance data; temper only problems with proven solutions. 
8.2.3. Learn Best Practices from the Best: 
o	While routes like Brisbane-Sydney show consistently high performance, learn from them. Use what they're doing right on these routes and adapt it to make all our operations tip-top! 
o	When routines are working well, just pass the word on to them all and there will be one standard high-performance mode which we can all cut easily.


8.2.4. Voice of Customers:
o	In every one of them, our passengers can recognize that American's service is special.
o	Data-Driven Information
o	Making timely and accurate information available to passengers can be used data-driven insights.
8.2.5. Regular Reviews:
o	General performance reviews allow you to measure the effectiveness of everything that has been implemented.
o	The insights that data from performance reviews provide to operational procedures can help to adjust them continuously and refine anything necessary. This results in more on-time arrival and departure times, fewer cancellations.
8.2.6. Seasonal, Monthly Analysis:
o	Pay attention to seasonal variations and monthly indicators. Identify months with high variability in on-time arrivals and departures. Develop strategies to alleviate those problems this winter.
o	Allocate additional people at busy times or in months which have historically bad records for service.



Conclusion
 
Virgin Australia may not have the best on-time record, but my analysis of flight performance suggests some are stronger and other areas need work. This allows an airline to identify which routes have excellent on-time performance and which routes continually suffer from delays and cancellations, and act accordingly to improve operations. These visualizations have yielded several practical benefits by giving Virgin Australia the ability to quickly make sense of data trends, respond to repeat incidents, as well as improve communication with customers. By looking at individual routes with a high cancellation rate and undertaking performance reviews the airline can drive more efficiently and guarantee a better passenger experience.


 References
 
Feibush, E., Gagvani, N. and Williams, D. (1999) ‘Geo-spatial visualization for situational awareness’, Proceedings Visualization ’99 (Cat. No.99CB37067) [Preprint]. doi:10.1109/visual.1999.809925. 
Isenberg, P. et al. (2011) ‘A study on dual-scale data charts’, IEEE Transactions on Visualization and Computer Graphics, 17(12), pp. 2469–2478. doi:10.1109/tvcg.2011.160. 
Jahns, V. (2014) ‘Information visualization’, ACM SIGSOFT Software Engineering Notes, 39(2), pp. 43–44. doi:10.1145/2579281.2579288. 
Keim, D.A. et al. (2009) ‘Generalized scatter plots’, Information Visualization, 9(4), pp. 301–311. doi:10.1057/ivs.2009.34. 
Pajankar, A. (2021) Practical python data visualization [Preprint]. doi:10.1007/978-1-4842-6455-3. 
Quach, Q. and Jenny, B. (2020) ‘Immersive visualization with Bar Graphics’, Cartography and Geographic Information Science, 47(6), pp. 471–480. doi:10.1080/15230406.2020.1771771. 
Tableau Software. (2024). ‘Tableau Dashboard and Story Creation.’ Retrieved from Tableau Documentation (no date) Tableau. Available at: https://www.tableau.com/products/new-features (Accessed: 05 June 2024). 
Wilkinson, L. and Friendly, M. (2009) ‘The history of the Cluster Heat Map’, The American Statistician, 63(2), pp. 179–184. doi:10.1198/tas.2009.0033.

