📊 Data Strategy & Preprocessing

The integrity of the predictive model relies on a high-quality dataset gathered through targeted extraction and rigorous filtration.

1. Data Acquisition

Method: Custom web scraping scripts were utilized to extract real-world listings from major secondary market automotive platforms.

Scope: Specifically focused on Audi vehicle variants across diverse regional markets to ensure brand-specific depreciation patterns.

2. Data Cleaning & Exclusion Criteria
To maintain model stability and prevent skewed estimations, the following data points were explicitly excluded from the training set:

Vintage Vehicles: Listings for models produced before 2010 were purged to focus on modern market dynamics.

Structural Integrity: Vehicles flagged with "Heavy Damage" (Ağır Hasarlı) or "Salvage Title" were removed to avoid outlier pricing.

Engine Modifications: Any vehicles with non-factory engine swaps or significant aftermarket mechanical modifications were deemed out-of-scope.

Incomplete Metadata: Listings missing critical features like transmission type, fuel format, or verifiable mileage were discarded.

3. Feature Engineering Highlights

Mileage-to-Age Ratio: A synthesized feature to identify "high-wear" vs. "well-preserved" vehicles.

Categorical Encoding: Audi-specific chassis and trim levels were preserved to capture the premium value associated with specific model configurations.
