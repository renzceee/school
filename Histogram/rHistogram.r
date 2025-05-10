library(tidyverse)
library(lubridate)
library(ggplot2)

df <- read.csv('Data.csv', stringsAsFactors = FALSE)

date_cols <- c('date_announced', 'date_recovered', 'date_of_death', 
               'date_announced_as_removed', 'date_of_onset_of_symptoms')

for (col in date_cols) {
  df[[col]] <- as.Date(df[[col]], format = "%Y-%m-%d")
}

hist(df$age, 
     main = "Distribution of Age", 
     xlab = "Age", 
     breaks = 20,
     col = "steelblue",
     border = "white")

ggplot(df, aes(x = age)) +
  geom_histogram(binwidth = 2, fill = "steelblue", color = "black", alpha = 0.7) +
  labs(title = "Distribution of Age",
       x = "Age",
       y = "Count") +
  theme_minimal()

ggplot(df, aes(x = age)) +
  geom_histogram(aes(y = ..density..), binwidth = 2, 
                 fill = "steelblue", color = "black", alpha = 0.7) +
  geom_density(alpha = 0.2, fill = "red") +
  labs(title = "Age Distribution with Density Curve",
       x = "Age",
       y = "Density") +
  theme_minimal()

ggplot(df, aes(x = age, fill = sex)) +
  geom_histogram(position = "stack", binwidth = 2, alpha = 0.7) +
  labs(title = "Age Distribution by Sex",
       x = "Age",
       y = "Count") +
  theme_minimal() +
  scale_fill_brewer(palette = "Set1")

df_dates <- df %>%
  filter(!is.na(date_announced)) %>%
  count(date_announced)

ggplot(df_dates, aes(x = date_announced, y = n)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  labs(title = "Number of Cases by Announcement Date",
       x = "Date",
       y = "Number of Cases") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

status_counts <- table(df$status)
barplot(status_counts, 
        main = "Distribution of Case Status",
        xlab = "Status",
        ylab = "Count",
        col = "steelblue")

df_long <- df %>%
  select(case_id, sex, status, age_group, health_status) %>%
  pivot_longer(cols = c(sex, status, age_group, health_status), 
               names_to = "variable", 
               values_to = "value")

ggplot(df_long, aes(x = value)) +
  geom_bar(fill = "steelblue") +
  facet_wrap(~ variable, scales = "free") +
  labs(title = "Distributions of Categorical Variables",
       x = NULL,
       y = "Count") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

library(plotly)

p <- ggplot(df, aes(x = age, fill = sex)) +
  geom_histogram(position = "stack", binwidth = 2, alpha = 0.7) +
  labs(title = "Interactive Age Distribution by Sex",
       x = "Age",
       y = "Count") +
  theme_minimal()

ggplotly(p)

top_provinces <- names(sort(table(df$province), decreasing = TRUE)[1:5])
province_df <- df[df$province %in% top_provinces, ]

ggplot(province_df, aes(x = age, fill = province)) +
  geom_histogram(position = "stack", binwidth = 2, alpha = 0.7) +
  labs(title = "Age Distribution in Top 5 Provinces",
       x = "Age",
       y = "Count") +
  theme_minimal() +
  scale_fill_brewer(palette = "Set1")