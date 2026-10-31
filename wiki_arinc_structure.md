![arinc-5-2](uploads/0a65d71a14f6edbd6ce29dfd34be7a0d/arinc-5-2.png){width=900 height=544}

**S - Standard (suitable for universal application)**

1 - S - Standard

2-4 Geographical area

5 - Section Code (SEC CODE)


<details>
<summary>5 - A - MORA</summary>

[//]: # (6)

- 6 - Subsection Code (SUB CODE)
  <details>
  <summary>6 - S - Grid MORA</summary>
  
  ![arinc-AS](uploads/f893ef221a73c62f7c63f52329ce7aaf/arinc-AS.png){width=312 height=600}

  **Grid MORA Primary Record (4.1.19.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Blank (Spacing) (3) | |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Subsection Code (1) | 5.5 |
  | 7-13 | Blank (Spacing) (7) | |
  | 14-16 | Starting Latitude (3) | 5.141 |
  | 17-20 | Starting Longitude (4) | 5.142 |
  | 21-30 | Blank (Spacing) (10) [^AS1] | |
  | 31-120 | 30 блоков MORA (3) | 5.143 |
  | 121-123 | Reserved (Expansion) (3) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  [^AS1]: В оригинале «21 thru 30 Blank (Spacing) (3)»; 21-30 — это 10 колонок.
  </details>

</details>
  


<details>
<summary>5 - D - Navaid</summary>
  
[//]: # (6)

- 6 - Subsection Code (SUB CODE)
  <details>
  <summary>6 - Blank - VHF Navaid</summary>
  
  ![arinc-DBlank](uploads/04607da5a25192c2d61d2b5554f42f86/arinc-DBlank.png){width=322 height=431}

  **Primary Record (4.1.2.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Subsection Code (1) | 5.5 |
  | 7-10 | Airport ICAO Identifier (4) | 5.6 |
  | 11-12 | ICAO Code (2) | 5.14 |
  | 13 | Blank (Spacing) (1) | |
  | 14-17 | VOR Identifier (4) | 5.33 |
  | 18-19 | Blank (Spacing) (2) | |
  | 20-21 | ICAO Code (2) | 5.14 |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23-27 | VOR Frequency (5) | 5.34 |
  | 28-32 | NAVAID Class (5) | 5.35 |
  | 33-41 | VOR Latitude (9) | 5.36 |
  | 42-51 | VOR Longitude (10) | 5.37 |
  | 52-55 | DME Ident (4) | 5.38 |
  | 56-64 | DME Latitude (9) | 5.36 |
  | 64-74 | DME Longitude (10) [^D1] | 5.37 |
  | 75-79 | Station Declination (5) | 5.66 |
  | 80-84 | DME Elevation (5) | 5.40 |
  | 85 | Figure of Merit (1) | 5.149 |
  | 86-87 | ILS/DME Bias (2) | 5.90 |
  | 88-90 | Frequency Protection (3) | 5.150 |
  | 91-93 | Datum Code (3) | 5.197 |
  | 94-123 | VOR Name (30) | 5.71 |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  [^D1]: В оригинале «64 thru 74»; по длине 10 корректный диапазон — 65-74.

  **Continuation Record (4.1.2.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23 | Reserved (Spacing) (1) | |
  | 24-92 | Notes (69) | 5.61 |
  | 93-123 | Reserved (Expansion) (31) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Simulation Continuation Record (4.1.2.3)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23 | Application Type (1) | 5.91 |
  | 24-27 | Blank (Spacing) (4) | |
  | 28-32 | Facility Characteristics (5) | 5.93 |
  | 33-74 | Reserved (Spacing) (42) | |
  | 75-79 | Magnetic Variation (5) | 5.39 |
  | 80-84 | Facility Elevation (5) | 5.92 |
  | 85-123 | Reserved (Expansion) (39) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Flight Planning Continuation Record (4.1.2.4)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23 | Application Type (1) | 5.91 |
  | 24-27 | FIR Identifier (4) | 5.116 |
  | 28-31 | UIR Identifier (4) | 5.116 |
  | 32 | Start/End Indicator (1) | 5.152 |
  | 33-43 | Start/End Date (11) | 5.153 |
  | 44-123 | Reserved (Expansion) (80) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Flight Planning Continuation Record (4.1.2.5)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23-123 | Fields as on Primary Records | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Limitation Continuation Record (4.1.2.6)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23 | Reserved (1) | |
  | 24 | Navaid Limitation Code (1) | 5.205 |
  | 25 | Component Affected Indicator (1) | 5.206 |
  | 26-27 | Sequence Number (2) | 5.12 |
  | 28-107 | 5 групп ограничений по 16 колонок: Sector From/Sector To (2) 5.207 → Distance Description (1) 5.187 → Distance Limitation (6) 5.208 → Altitude Description (1) 5.29 → Altitude Limitation (6) 5.209 | |
  | 108 | Sequence End Indicator (1) | 5.210 |
  | 109-123 | Blank (Spacing) (15) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>

  <details>
  <summary>6 - B - NDB Navaid</summary>
  
  ![arinc-DB](uploads/1c7f6e0c3830e2bc555daeed91368de5/arinc-DB.png){width=328 height=363}

  **Primary Record (4.1.3.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Subsection Code (1) | 5.5 |
  | 7-10 | Airport ICAO Identifier (4) | 5.6 |
  | 11-12 | ICAO Code (2) | 5.14 |
  | 13 | Blank (Spacing) (1) | |
  | 14-17 | NDB Identifier (4) | 5.33 |
  | 18-19 | Blank (Spacing) (2) | |
  | 20-21 | ICAO Code (2) | 5.14 |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23-27 | NDB Frequency (5) | 5.34 |
  | 28-32 | NDB Class (5) | 5.35 |
  | 33-41 | NDB Latitude (9) | 5.36 |
  | 42-51 | NDB Longitude (10) | 5.37 |
  | 52-74 | Blank (Spacing) (6) [^D2] | |
  | 75-79 | Magnetic Variation (5) | 5.39 |
  | 80-85 | Blank (Spacing) (6) | |
  | 86-90 | Reserved (Expansion) (5) | |
  | 91-93 | Datum Code (3) | 5.197 |
  | 94-123 | NDB Name (30) | 5.71 |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  [^D2]: В оригинале «52 thru 74» при указанной длине 6 (по длине сходится 52-57); колонки 58-74 в источнике не описаны отдельной строкой — вероятно, также Blank.

  **Continuation Record (4.1.3.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23 | Reserved (Spacing) (1) | |
  | 24-92 | Notes (69) | 5.61 |
  | 93-123 | Reserved (Expansion) (31) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Simulation Continuation Record (4.1.3.3)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23 | Application Type (1) | 5.91 |
  | 24-27 | Blank (Spacing) (4) | |
  | 28-32 | Facility Characteristics (5) | 5.93 |
  | 33-79 | Reserved (Spacing) (47) | |
  | 80-84 | Facility Elevation (5) | 5.92 |
  | 85-123 | Reserved (Expansion) (39) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Flight Planning Continuation Record (4.1.3.4)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23 | Application Type (1) | 5.91 |
  | 24-27 | FIR Identifier (4) | 5.116 |
  | 28-31 | UIR Identifier (4) | 5.116 |
  | 32 | Start/End Indicator (1) | 5.152 |
  | 33-43 | Start/End Date (11) | 5.153 |
  | 44-123 | Reserved (Expansion) (80) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Flight Planning Continuation Record (4.1.3.5)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23-123 | Fields as on Primary Records | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>

</details>


<details>
<summary>5 - E - Enroute</summary>
  
[//]: # (6)

- 6 - Subsection Code (SUB CODE)
  <details>
  <summary>6 - A - Waypoints (EA)</summary>
  
  ![arinc-EA](uploads/a730da9736ce18eb027bf2fe064fa65c/arinc-EA.png){width=327 height=405}

  **Holding Pattern Waypoint Primary Record (4.1.4.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Subsection Code (1) [^EA1] | 5.5 |
  | 7-10 | Region Code (4) [^EA2] | 5.41 |
  | 11-12 | ICAO Code (2) | 5.14 |
  | 13 | Subsection (1) [^EA1] | 5.5 |
  | 14-18 | Waypoint Identifier (5) | 5.13 |
  | 19 | Blank (Spacing) (1) | |
  | 20-21 | ICAO Code (2) | 5.14 |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23-26 | Blank (Spacing) (4) | |
  | 27-29 | Waypoint Type (3) | 5.42 |
  | 30-31 | Waypoint Usage (2) | 5.82 |
  | 32 | Blank (Spacing) (1) | |
  | 33-41 | Waypoint Latitude (9) | 5.36 |
  | 42-51 | Waypoint Longitude (10) | 5.37 |
  | 52-74 | Blank (Spacing) (23) | |
  | 75-79 | Dynamic Mag. Variation (5) | 5.39 |
  | 80-84 | Reserved (Expansion) (5) | |
  | 85-87 | Datum Code (3) | 5.197 |
  | 88-95 | Reserved (Expansion) (8) | |
  | 96-98 | Name Format Indicator (3) | 5.196 |
  | 99-123 | Waypoint Name/Description (25) | 5.43 |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  [^EA1]: В Enroute Waypoint Records Subsection Code занимает колонку 6, колонка 13 — blank. В Airport/Heliport Terminal Waypoint Records Subsection Code занимает колонку 13, колонка 6 — blank.

  [^EA2]: В Enroute Waypoint records используется код «ENRT». В Terminal Waypoint records поле содержит Airport ICAO Identification code.

  **Waypoint Continuation Record (4.1.4.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23 | Reserved (Spacing) (1) | |
  | 24-92 | Notes (69) | 5.61 |
  | 93-123 | Reserved (Expansion) (31) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  Примечание: колонка 23 зарезервирована под символ кода приложения.

  **Waypoint Flight Planning Continuation Record (4.1.4.3)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23 | Application Type (1) | 5.91 |
  | 24-27 | FIR Identifier (4) | 5.116 |
  | 28-31 | UIR Identifier (4) | 5.116 |
  | 32 | Start/End Indicator (1) | 5.152 |
  | 33-43 | Start/End Date (11) | 5.153 |
  | 44-123 | Reserved (Expansion) (80) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Waypoint Flight Planning Continuation Record (4.1.4.4)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23-123 | Fields as on Primary Records | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>

  <details>
  <summary>6 - M - Airway Markers (EM)</summary>
  
  ![arinc-EM](uploads/272440ea9b6ab4afd407918ccacbc248/arinc-EM.png){width=327 height=314}

  **Airways Marker Primary Record (4.1.15.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Subsection Code (1) | 5.5 |
  | 7-13 | Blank (Spacing) (7) | |
  | 14-17 | Marker Identifier (4) | 5.110 |
  | 18-19 | Blank (Spacing) (2) | |
  | 20-21 | ICAO Code (2) | 5.14 |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23-26 | Marker Code (4) | 5.111 |
  | 27 | Reserved (Expansion) (1) | |
  | 28 | Marker Shape (1) | 5.112 |
  | 29 | Marker Power (1) | 5.113 |
  | 30-32 | Blank (Spacing) (2) | |
  | 33-41 | Marker Latitude (9) | 5.36 |
  | 42-51 | Marker Longitude (10) | 5.37 |
  | 52-55 | Minor Axis (4) | 5.100 |
  | 56-74 | Blank (Spacing) (19) | |
  | 75-79 | Magnetic Variation (5) | 5.39 |
  | 80-84 | Facility Elevation (5) | 5.92 |
  | 85-87 | Datum Code (3) | 5.197 |
  | 88-93 | Blank (Spacing) (6) | |
  | 94-123 | Marker Name (30) | 5.71 |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>

  <details>
  <summary>6 - P - Holding Patterns (EP)</summary>
  
  ![arinc-EP](uploads/a03e9b380e3d0b63119c1e8f35bb8800/arinc-EP.png){width=331 height=376}

  **Holding Primary Record (4.1.5.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Subsection Code (1) | 5.5 |
  | 7-10 | Region Code (4) [^EP1] | 5.41 |
  | 11-12 | ICAO Code (2) | 5.14 |
  | 13-27 | Blank (Spacing) (15) | |
  | 28-29 | Duplicate Identifier (2) | 5.114 |
  | 30-34 | Fix Identifier (5) | 5.13 |
  | 35-36 | ICAO Code (2) | 5.14 |
  | 37 | Section Code (1) | 5.4 |
  | 38 | Subsection Code (1) | 5.5 |
  | 39 | Continuation Record No. (1) | 5.16 |
  | 40-43 | Inbound Holding Course (4) | 5.62 |
  | 44 | Turn Direction (1) | 5.63 |
  | 45-47 | Leg Length (3) | 5.64 |
  | 48-49 | Leg Time (2) | 5.65 |
  | 50-54 | Minimum Altitude (5) | 5.30 |
  | 55-59 | Maximum Altitude (5) | 5.127 |
  | 60-62 | Holding Speed (3) | 5.175 |
  | 63-98 | Reserved (Expansion) (36) | |
  | 99-123 | Notes (25) | 5.60 |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  [^EP1]: В Enroute Fix Holding Pattern records в Region Code используется код «ENRT», ICAO Code — blank. В Terminal Fix Holding record Region Code содержит идентификатор Airport или Heliport, с которым связан holding; ICAO Code не blank. Это однозначно идентифицирует Terminal NDB, Airport Terminal Waypoint или Heliport Terminal Waypoint.

  **Holding Pattern Continuation Record (4.1.5.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-38 | Fields as on Primary Records | |
  | 39 | Continuation Record No. (1) | 5.16 |
  | 40 | Reserved (Spacing) (1) | |
  | 41-109 | Notes (69) | 5.61 |
  | 110-123 | Reserved (Expansion) (14) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  Примечание: колонка 40 зарезервирована под символ кода приложения.
  </details>

  <details>
  <summary>6 - R - Airways and Routes (ER)</summary>
  
  ![arinc-ER](uploads/925d1bb048257552c6a89ca24a0d104a/arinc-ER.png){width=339 height=562}

  **Enroute Airways Primary Record (4.1.6.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Subsection Code (1) | 5.5 |
  | 7-13 | Blank (Spacing) (7) | |
  | 14-18 | Route Identifier (5) | 5.8 |
  | 19 | Reserved (1) [^ER1] | |
  | 20-25 | Blank (Spacing) (6) | |
  | 26-29 | Sequence Number (4) | 5.12 |
  | 30-34 | Fix Identifier (5) | 5.13 |
  | 35-36 | ICAO Code (2) | 5.14 |
  | 37 | Section Code (1) | 5.4 |
  | 38 | Subsection (1) | 5.5 |
  | 39 | Continuation Record No. (1) | 5.16 |
  | 40-43 | Waypoint Description Code (4) | 5.17 |
  | 44 | Boundary Code (1) | 5.18 |
  | 45 | Route Type (1) | 5.7 |
  | 46 | Level (1) | 5.19 |
  | 47 | Direction Restriction (1) | 5.115 |
  | 48-49 | Cruise Table Indicator (2) | 5.134 |
  | 50 | EU Indicator (1) | 5.164 |
  | 51-54 | Recommended NAVAID (4) | 5.23 |
  | 55-56 | ICAO Code (2) | 5.14 |
  | 57-59 | RNP (3) | 5.211 |
  | 60-62 | Blank (Spacing) (3) | |
  | 63-66 | Theta (4) | 5.24 |
  | 67-70 | Rho (4) | 5.25 |
  | 71-74 | Outbound Magnetic Course (4) | 5.26 |
  | 75-78 | Route Distance From (4) | 5.27 |
  | 79-82 | Inbound Magnetic Course (4) | 5.28 |
  | 83 | Blank (Spacing) (1) | |
  | 84-88 | Minimum Altitude (5) | 5.30 |
  | 89-93 | Minimum Altitude (5) | 5.30 |
  | 94-98 | Maximum Altitude (5) | 5.127 |
  | 99-123 | Reserved (Expansion) (25) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  [^ER1]: Стандартная длина Route Identifier — пять символов; зарезервированная колонка 19 допускает шестисимвольное поле. Некоторые поставщики данных используют эту позицию для суффикса ATS Service.

  **Enroute Airways Continuation Record (4.1.6.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-38 | Fields as on Primary Records | |
  | 39 | Continuation Record No. (1) | 5.16 |
  | 40 | Reserved (Spacing) (1) | |
  | 41-109 | Notes (69) | 5.61 |
  | 110-123 | Reserved (Expansion) (14) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  Примечание: колонка 40 зарезервирована под символ кода приложения.

  **Enroute Airways Flight Planning Continuation Record (4.1.6.3)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-38 | Fields as on Primary Records | |
  | 39 | Continuation Record No. (1) | 5.16 |
  | 40 | Application Type (1) | 5.91 |
  | 41 | Start/End Indicator (1) | 5.152 |
  | 42-52 | Start/End Date (11) | 5.153 |
  | 53-66 | Blank (Spacing) (14) | |
  | 67-122 | 4 группы по 14 колонок: Restr. Airspace ICAO Code (2) 5.14 → Restr. Airspace Type (1) 5.128 → Restr. Airspace Designation (10) 5.129 → Restr. Airspace Multiple Code (1) 5.130 | |
  | 123 | Restr. Airspace Link Continuation (1) | 5.174 |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Enroute Airways Flight Planning Continuation Record (4.1.6.4)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-38 | Fields as on Primary Records | |
  | 39 | Continuation Record No. (1) | 5.16 |
  | 40-123 | Fields as on Primary Records | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>

  <details>
  <summary>6 - T - Preferred Routes (ET)</summary>
  
  ![arinc-ET](uploads/978241495976b9d355a09db1d9b0365b/arinc-ET.png){width=325 height=591}

  **Preferred Route Primary Record (4.1.24.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Subsection Code (1) | 5.5 |
  | 7-13 | Blank (Spacing) (7) | |
  | 14-23 | Route Identifier (10) | 5.8 |
  | 24-25 | Preferred Route Use Ind (2) | 5.220 |
  | 26-29 | Sequence Number (4) | 5.12 |
  | 30-38 | Blank (Spacing) (9) | |
  | 39 | Continuation Record No. (1) | 5.16 |
  | 40-44 | To Fix Identifier (5) | 5.83 |
  | 45-46 | ICAO Code (2) | 5.14 |
  | 47 | Section Code (1) | 5.4 |
  | 48 | Subsection Code (1) | 5.5 |
  | 49-51 | VIA Code (3) | 5.77 |
  | 52-57 | SID/STAR/AWY Ident (6) [^ET1] | 5.78 |
  | 58-60 | AREA Code (3) | 5.3 |
  | 61 | Level (1) | 5.19 |
  | 62 | Route Type (1) | 5.7 |
  | 63-67 | Initial Airport/Fix (5) | 5.194 |
  | 68-69 | ICAO Code (2) | 5.14 |
  | 70 | Section Code (1) | 5.4 |
  | 71 | Subsection Code (1) | 5.5 |
  | 72-76 | Terminus Airport/Fix (5) | 5.194 |
  | 77-78 | ICAO Code (2) | 5.14 |
  | 79 | Section Code (1) | 5.4 |
  | 80 | Subsection Code (1) | 5.5 |
  | 81-85 | Minimum Altitude (5) | 5.30 |
  | 86-90 | Maximum Altitude (5) | 5.127 |
  | 91 | Time Code (1) | 5.131 |
  | 92-93 | Aircraft Use Group (2) | 5.221 |
  | 94 | Direction Restriction (1) | 5.115 |
  | 95 | Altitude Description (1) | 5.29 |
  | 96-100 | Altitude One (5) | 5.30 |
  | 101-105 | Altitude Two (5) | 5.30 |
  | 106-123 | Reserved (Expansion) (18) | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  [^ET1]: Standard Enroute Airway Identifier — пять символов; длина поля допускает шестисимвольное кодирование (см. 5.8).

  **Preferred Route Continuation Record (4.1.24.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-38 | Fields as on Primary Records | |
  | 39 | Continuation Record No. (1) | 5.16 |
  | 40 | Reserved Spacing (1) | |
  | 41 | Time Code (1) | 5.131 |
  | 42 | Time Indicator | 5.138 |
  | 43-112 | 7 блоков Time of Operation (10) | 5.195 |
  | 113-123 | Reserved (Expansion) (11) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Preferred Route Continuation Record (4.1.24.3)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-38 | Fields as on Primary Records | |
  | 39 | Continuation Record No. (1) | 5.16 |
  | 40 | Reserved (Spacing) (1) | |
  | 41-109 | Notes (69) | 5.61 |
  | 110-123 | Reserved (Expansion) (14) | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  Примечание: использование этой записи для Aircraft Use Groups описано в 5.221.
  </details>

  <details>
  <summary>6 - U - Airway Restrictions (EU)</summary>
  
  ![arinc-EU](uploads/361f0c86cf8d8ee196ad78f6ec19679c/arinc-EU.png){width=305 height=600}

  **Altitude Exclusion Primary Record (4.1.21.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Subsection Code (1) | 5.5 |
  | 7-11 | Route Identifier (5) | 5.8 |
  | 12 | Reserved (1) [^EU1] | |
  | 13-15 | Restriction Identifier (3) | 5.154 |
  | 16-17 | Restriction Type (2) | 5.201 |
  | 18 | Continuation Record No. (1) | 5.16 |
  | 19-23 | Start Fix Identifier (5) | 5.13 |
  | 24-25 | Start Fix ICAO Code (2) | 5.14 |
  | 26 | Start Fix Section Code (1) | 5.4 |
  | 27 | Start Fix Subsection Code (1) | 5.5 |
  | 28-32 | End Fix Identifier (5) | 5.13 |
  | 33-34 | End Fix ICAO Code (2) | 5.14 |
  | 35 | End Fix Section Code (1) | 5.4 |
  | 36 | End Fix Subsection Code (1) | 5.5 |
  | 37 | Blank (Spacing) (1) | |
  | 38-44 | Start Date (7) | 5.157 |
  | 45-51 | End Date (7) | 5.157 |
  | 52 | Time Code (1) | 5.131 |
  | 53 | Time Indicator (1) | 5.138 |
  | 54-63 | Time of Operation (10) | 5.195 |
  | 64-73 | Time of Operation (10) | 5.195 |
  | 74-83 | Time of Operation (10) | 5.195 |
  | 84-93 | Time of Operation (10) | 5.195 |
  | 94 | Exclusion Indicator (1) | 5.202 |
  | 95 | Units of Altitude (1) | 5.160 |
  | 96-98 | Restriction Altitude (3) | 5.161 |
  | 99 | Block Indicator (1) | 5.203 |
  | 100-102 | Restriction Altitude (3) | 5.161 |
  | 103 | Block Indicator (1) | 5.203 |
  | 104-106 | Restriction Altitude (3) | 5.161 |
  | 107 | Block Indicator (1) | 5.203 |
  | 108-110 | Restriction Altitude (3) | 5.161 |
  | 111 | Block Indicator (1) | 5.203 |
  | 112-114 | Restriction Altitude (3) | 5.161 |
  | 115 | Block Indicator (1) | 5.203 |
  | 116-118 | Restriction Altitude (3) | 5.161 |
  | 119 | Block Indicator (1) | 5.203 |
  | 120-122 | Restriction Altitude (3) | 5.161 |
  | 123 | Blank (Spacing) (1) | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  [^EU1]: Стандартная длина Route Identifier — пять символов; зарезервированная колонка 12 допускает шестисимвольное поле.

  **Altitude Exclusion Continuation Record (4.1.21.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-17 | Fields as on Primary Records | |
  | 18 | Continuation Record No. (1) | 5.16 |
  | 19-51 | Reserved (Expansion) (33) | |
  | 52 | Time Code (1) | 5.131 |
  | 53 | Time Indicator (1) | 5.138 |
  | 54-93 | 4 блока Time of Operation (10) | 5.195 |
  | 94 | Exclusion Indicator (1) | 5.202 |
  | 95 | Units of Altitude (1) | 5.160 |
  | 96-122 | 7 групп: Restriction Altitude (3) 5.161 → Block Indicator (1) 5.203 | |
  | 123 | Blank (Spacing) (1) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Note Restriction Primary Record (4.1.21A.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Subsection Code (1) | 5.5 |
  | 7-11 | Route Identifier (5) | 5.8 |
  | 12 | Reserved (1) [^EU1] | |
  | 13-15 | Restriction Identifier (3) | 5.154 |
  | 16-17 | Restriction Type (2) | 5.201 |
  | 18 | Continuation Record No. (1) | 5.16 |
  | 19-23 | Start Fix Identifier (5) | 5.13 |
  | 24-25 | Start Fix ICAO Code (2) | 5.14 |
  | 26 | Start Fix Section Code (1) | 5.4 |
  | 27 | Start Fix Subsection Code (1) | 5.5 |
  | 28-32 | End Fix Identifier (5) | 5.13 |
  | 33-34 | End Fix ICAO Code (2) | 5.14 |
  | 35 | End Fix Section Code (1) | 5.4 |
  | 36 | End Fix Subsection Code (1) | 5.5 |
  | 37 | Blank (Spacing) (1) | |
  | 38-44 | Start Date (7) | 5.157 |
  | 45-51 | End Date (7) | 5.157 |
  | 52-120 | Restriction Notes (69) | 5.163 |
  | 121-123 | Blank (Spacing) (3) | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Note Restriction Continuation Record (4.1.21A.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-17 | Fields as on Primary Records | |
  | 18 | Continuation Record No. (1) | 5.16 |
  | 19-51 | Reserved (Expansion) (33) | |
  | 52-120 | Restriction Notes (69) | 5.163 |
  | 121-123 | Blank (Spacing) (3) | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Seasonal Closure Primary Record (4.1.21B.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Subsection Code (1) | 5.5 |
  | 7-11 | Route Identifier (5) | 5.8 |
  | 12 | Reserved (1) [^EU1] | |
  | 13-15 | Restriction Identifier (3) | 5.154 |
  | 16-17 | Restriction Type (2) | 5.201 |
  | 18 | Continuation Record No. (1) | 5.16 |
  | 19-23 | Start Fix Identifier (5) | 5.13 |
  | 24-25 | Start Fix ICAO Code (2) | 5.14 |
  | 26 | Start Fix Section Code (1) | 5.4 |
  | 27 | Start Fix Subsection Code (1) | 5.5 |
  | 28-32 | End Fix Identifier (5) | 5.13 |
  | 33-34 | End Fix ICAO Code (2) | 5.14 |
  | 35 | End Fix Section Code (1) | 5.4 |
  | 36 | End Fix Subsection Code (1) | 5.5 |
  | 37 | Blank (Spacing) (1) | |
  | 38-44 | Start Date (7) | 5.157 |
  | 45-51 | End Date (7) | 5.157 |
  | 52 | Time Code (1) | 5.131 |
  | 53 | Time Indicator (1) | 5.138 |
  | 54-93 | 4 блока Time of Operation (10) | 5.195 |
  | 94-95 | Cruise Table Ident (2) | 5.134 |
  | 96-123 | Blank (Spacing) (28) | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Cruising Table Replacement Primary Record (4.1.21C.1)** — то же, что Seasonal Closure Primary

  **Cruising Table Replacement Continuation Record (4.1.21C.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-17 | Fields as on Primary Records | |
  | 18 | Continuation Record No. (1) | 5.16 |
  | 19-51 | Reserved (Expansion) (33) | |
  | 52 | Time Code (1) | 5.131 |
  | 53 | Time Indicator (1) | 5.138 |
  | 54-93 | 4 блока Time of Operation (10) | 5.195 |
  | 94-95 | Cruise Table Ident (2) | 5.134 |
  | 96-123 | Blank (Spacing) (28) | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>

  <details>
  <summary>6 - V - Communications (EV)</summary>
  
  ![arinc-EV](uploads/eba479780caab4c96b3ab0d6ae2fd523/arinc-EV.png){width=326 height=449}

  **Enroute Communications Primary Record (4.1.23.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Subsection Code (1) | 5.5 |
  | 7-10 | FIR/RDO Ident (4) | 5.190 |
  | 11-14 | FIR/UIR Address (4) | 5.151 |
  | 15 | Indicator (1) | 5.117 |
  | 16-18 | Reserved (Expansion) (3) | |
  | 19-43 | Remote Name (25) | 5.189 |
  | 44-46 | Communications Type (3) | 5.101 |
  | 47-53 | Comm Frequency (7) | 5.103 |
  | 54 | Guard/Transmit (1) | 5.182 |
  | 55 | Frequency Units (1) | 5.104 |
  | 56 | Continuation Record No. (1) | 5.16 |
  | 57-59 | Service Indicator (3) | 5.106 |
  | 60 | Radar Service (1) | 5.102 |
  | 61 | Modulation (1) | 5.198 |
  | 62 | Signal Emission (1) | 5.199 |
  | 63-71 | Latitude (9) | 5.36 |
  | 72-81 | Longitude (10) | 5.37 |
  | 82-86 | Magnetic Variation (5) | 5.39 |
  | 87-91 | Facility Elevation (5) | 5.92 |
  | 92 | H24 Indicator (1) | 5.181 |
  | 93 | Altitude Descript. (1) | 5.29 |
  | 94-98 | Communication Altitude (5) | 5.184 |
  | 99-103 | Communication Altitude (5) | 5.184 |
  | 104-107 | Remote Facility (4) | 5.200 |
  | 108-109 | ICAO Code (2) | 5.14 |
  | 110 | Section Code (1) | 5.4 |
  | 111 | Subsection Code (1) | 5.5 |
  | 112-123 | Reserved (Expansion) (12) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Enroute Communications Continuation Record (4.1.23.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-55 | Fields as on Primary Records | |
  | 56 | Continuation Record No. (1) | 5.16 |
  | 57 | Blank (Spacing) (1) | |
  | 58 | Time Code (1) | 5.131 |
  | 59 | NOTAM (1) | 5.132 |
  | 60 | Time Indicator (1) | 5.138 |
  | 61-70 | Time of Operation (10) | 5.195 |
  | 71-83 | Reserved (Expansion) (23) [^EV1] | |
  | 84-123 | Call Sign (30) | 5.105 |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  [^EV1]: В оригинале «71 thru 83 Reserved (Expansion) (23)» — 71-83 это 13 колонок; и Call Sign (30) при длине 25 в 5.105. Так в источнике.

  **Enroute Communications Continuation Record (4.1.23.3)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-55 | Fields as on Primary Records | |
  | 56 | Continuation Record No. (1) | 5.16 |
  | 57-60 | Blank (Spacing) (4) | |
  | 61-120 | 6 блоков Time of Operation (10) | 5.195 |
  | 121-123 | Reserved (Expansion) (3) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>
</details>
  


<details>
<summary>5 - H - Heliport</summary>
  
[//]: # (6)

- 6 - Blank
- 7-10 - Region Code or Airport ICAO Identifier 
- 11-12 - ICAO Code
- 13 - Subsection Code
  <details>
  <summary>13 - A - Waypoints (HA)</summary>
  
  ![arinc-HA](uploads/8ecea1ec0801cd1a5bdbb5b9bf7e4094/arinc-HA.png){width=312 height=491}

  **Heliport Primary Record (4.2.1.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Blank (Spacing) (1) | |
  | 7-10 | Heliport Identifier (4) | 5.6 |
  | 11-12 | ICAO Code (2) | 5.14 |
  | 13 | Subsection Code (1) | 5.5 |
  | 14-16 | ATA/IATA Designator (3) | 5.107 |
  | 17-21 | PAD Identifier (5) | 5.180 |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23-27 | Speed Limit Altitude (5) | 5.73 |
  | 28-30 | Datum Code (3) | 5.197 |
  | 31 | IFR Indicator (1) | 5.108 |
  | 32 | Blank (Spacing) (1) | |
  | 33-41 | Latitude (9) | 5.36 |
  | 42-51 | Longitude (10) | 5.37 |
  | 52-56 | Magnetic Variation (5) | 5.39 |
  | 57-61 | Heliport Elevation (5) | 5.55 |
  | 62-64 | Speed Limit (3) | 5.72 |
  | 65-68 | Recommended VHF Navaid (4) | 5.23 |
  | 69-70 | ICAO Code (2) | 5.14 |
  | 71-75 | Transition Altitude (5) | 5.53 |
  | 76-80 | Transition Level (5) | 5.53 |
  | 81 | Public Military Indicator (1) | 5.177 |
  | 82-84 | Time Zone (3) | 5.178 |
  | 85 | Daylight Indicator (1) | 5.179 |
  | 86-91 | Pad Dimensions (6) | 5.176 |
  | 92 | Magnetic/True Indicator (1) | 5.165 |
  | 93 | Reserved (Expansion) (1) | |
  | 94-123 | Heliport Name (30) | 5.71 |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Heliport Continuation Record (4.2.1.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23 | Reserved (Spacing) (1) | |
  | 24-92 | Notes (69) | 5.61 |
  | 93-123 | Reserved (Expansion) (31) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Heliport Flight Planning Continuation Record (4.2.1.3)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record Number (1) | 5.16 |
  | 23 | Application Type (1) | 5.91 |
  | 24-27 | FIR Identifier (4) | 5.116 |
  | 28-31 | UIR Identifier (4) | 5.116 |
  | 32 | Start/End Indicator (1) | 5.152 |
  | 33-43 | Start/End Date/Time (11) | 5.153 |
  | 44-66 | Blank (Spacing) (23) | |
  | 67 | Controlled A/S Indicator (1) | 5.217 |
  | 68-71 | Controlled A/S Airport Identifier (4) | 5.6 |
  | 72-73 | Controlled A/S Airport ICAO (2) | 5.14 |
  | 74-123 | Blank (Spacing) (50) | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Heliport Flight Planning Continuation Record (4.2.1.4)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23-123 | Fields as on Primary Records | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>

  <details>
  <summary>13 - C - Terminal Waypoints (HC)</summary>
  
  ![arinc-HC](uploads/6ab79d46abfb2c95b1eebafddc5721ec/arinc-HC.png){width=336 height=408}

  **Heliport Terminal Waypoint Primary Record (4.2.2.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Blank (Spacing) (1) | |
  | 7-10 | Heliport Identifier (4) | 5.6 |
  | 11-12 | ICAO Code (2) | 5.14 |
  | 13 | Subsection Code (1) | 5.5 |
  | 14-18 | Waypoint Identifier (5) | 5.13 |
  | 19 | Blank (Spacing) (1) | |
  | 20-21 | ICAO Code (2) | 5.14 |
  | 22 | Continuation Record Number (1) | 5.16 |
  | 23-26 | Blank (Spacing) (4) | |
  | 27-29 | Waypoint Type (3) | 5.42 |
  | 30-31 | Waypoint Usage (2) | 5.82 |
  | 32 | Blank (Spacing) (1) | |
  | 33-41 | Waypoint Latitude (9) | 5.36 |
  | 42-51 | Waypoint Longitude (10) | 5.37 |
  | 52-74 | Blank (Spacing) (23) | |
  | 75-79 | Dynamic Magnetic Variation (5) | 5.39 |
  | 80-84 | Reserved (Expansion) (5) | |
  | 85-87 | Datum Code (3) | 5.197 |
  | 88-95 | Reserved (Expansion) (8) | |
  | 96-98 | Name Format Indicator (3) | 5.196 |
  | 99-123 | Waypoint Name/Description (25) | 5.43 |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Heliport Terminal Waypoint Continuation Record (4.2.2.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record Number (1) | 5.16 |
  | 23 | Reserved (Spacing) (1) | |
  | 24-92 | Notes (69) | 5.61 |
  | 93-123 | Reserved (Expansion) (31) | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  Примечание: колонка 23 зарезервирована под символ Application Type.

  **Heliport Terminal Waypoint Flight Planning Continuation Record (4.2.2.3)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record Number (1) | 5.16 |
  | 23 | Application Type (1) | 5.91 |
  | 24-27 | FIR Identifier (4) | 5.116 |
  | 28-31 | UIR Identifier (4) | 5.116 |
  | 32 | Start/End Indicator (1) | 5.152 |
  | 33-43 | Start/End Date (11) | 5.153 |
  | 44-123 | Reserved (Expansion) (80) [^HC1] | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  [^HC1]: В оригинале «44 thru 123 Reserved (Expansion) (31)» — 44-123 это 80 колонок.

  **Heliport Terminal Waypoint Flight Planning Continuation Record (4.2.2.4)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record Number (1) | 5.16 |
  | 23-123 | Fields as on Primary Records | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>

  <details>
  <summary>13 - D - SIDs (HD)</summary>
  
  ![arinc-HD](uploads/71360530710022352a17af2733b222d0/arinc-HD.png){width=264 height=600}

  **Heliport SID/STAR/Approach Primary Record (4.2.3.1)** — макет общий для HD/HE/HF

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Blank (Spacing) (1) | |
  | 7-10 | Heliport Identifier (4) | 5.6 |
  | 11-12 | ICAO Code (2) | 5.14 |
  | 13 | Subsection Code (1) | 5.5 |
  | 14-19 | SID/STAR/APP Identifier (6) | 5.9, 5.10 |
  | 20 | Route Type (1) | 5.7 |
  | 21-25 | Transition Identifier (5) | 5.11 |
  | 26 | Multiple Indicator (1) [^HD1] | 5.130 |
  | 27-29 | Sequence Number (3) | 5.12 |
  | 30-34 | Fix Identifier (5) | 5.13 |
  | 35-36 | ICAO Code (2) | 5.14 |
  | 37 | Section Code (1) | 5.4 |
  | 38 | Subsection Code (1) | 5.5 |
  | 39 | Continuation Record Number (1) | 5.16 |
  | 40-43 | Waypoint Description Code (4) | 5.17 |
  | 44 | Turn Direction (1) | 5.20 |
  | 45-47 | RNP (3) | 5.211 |
  | 48-49 | Path and Termination (2) | 5.21 |
  | 50 | Turn Direction Valid (1) | 5.22 |
  | 51-54 | Recommended Navaid (4) | 5.23 |
  | 55-56 | ICAO Code (2) | 5.14 |
  | 57-62 | ARC Radius (6) | 5.204 |
  | 63-66 | Theta (4) | 5.24 |
  | 67-70 | Rho (4) | 5.25 |
  | 71-74 | Magnetic Course (4) | 5.26 |
  | 75-78 | Route Distance/Holding Distance or Time (4) | 5.27 |
  | 79 | Recommended Navaid Section (1) | 5.4 |
  | 80 | Recommended Navaid Subsection (1) | 5.5 |
  | 81-82 | Reserved (Spacing) (2) | |
  | 83 | Altitude Description (1) | 5.29 |
  | 84 | ATC Indicator (1) | 5.81 |
  | 85-89 | Altitude (5) | 5.30 |
  | 90-94 | Altitude (5) | 5.30 |
  | 95-99 | Transition Altitude (5) | 5.53 |
  | 100-102 | Speed Limit (3) | 5.72 |
  | 103-106 | Vertical Angle (4) | 5.70 |
  | 107-111 | Center Fix (5) | 5.144 |
  | 112 | Multiple Code (1) | 5.130 |
  | 113-114 | ICAO Code (2) | 5.14 |
  | 115 | Section Code (1) | 5.4 |
  | 116 | Subsection Code (1) | 5.5 |
  | 117 | GPS/FMS Indicator (1) | 5.222 |
  | 118 | Blank (Spacing) (1) | |
  | 119 | Apch Route Qualifier 1 (1) | 5.7 |
  | 120 | Apch Route Qualifier 2 (1) | 5.7 |
  | 121-123 | Blank (Spacing) (3) | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  [^HD1]: Multiple Indicator используется только в Approach Procedures.

  **Heliport SID/STAR/Approach Continuation Record (4.2.3.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-38 | Field as on Primary Records | |
  | 39 | Continuation Record Number (1) | 5.16 |
  | 40 | Reserved (Spacing) (1) | |
  | 41-44 | CAT A Decision Height (4) | 5.170 |
  | 45-48 | CAT B Decision Height (4) | 5.170 |
  | 49-52 | CAT C Decision Height (4) | 5.170 |
  | 53-56 | CAT D Decision Height (4) | 5.170 |
  | 57-60 | CAT A Minimum Descent Height (4) | 5.171 |
  | 61-64 | CAT B Minimum Descent Height (4) | 5.171 |
  | 65-68 | CAT C Minimum Descent Height (4) | 5.171 |
  | 69-72 | CAT D Minimum Descent Height (4) | 5.171 |
  | 73-85 | Blank (Spacing) (13) | |
  | 86-89 | Procedure Category (4) | 5.242 |
  | 90-92 | RNP (3) | 5.211 |
  | 93-118 | Reserved (Expansion) (26) [^HD2] | |
  | 119 | Apch Route Qualifier 1 (1) | 5.7 |
  | 120 | Apch Route Qualifier 2 (1) | 5.7 |
  | 121-123 | Blank (Spacing) (3) | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  [^HD2]: В оригинале указана длина (25); 93-118 — это 26 колонок (в 4.1.9.2 — (26)).

  Примечания:
  1. Колонка 40 зарезервирована под символ Application Type.
  2. Колонки 119 и 120 — часть ключа сортировки для сопоставления Continuation Records с Primary Record; нестандартная сортировка выбрана для сохранения Primary Record, введена в Supplement 14.
  3. Для записей «All Sensors RNAV» RNP находится в колонках 90-92 Continuation Record и связан с Procedure Category; RNP в колонках 45-47 Primary Record — blank.

  **Heliport SID/STAR/Approach Flight Planning Continuation Record (4.2.3.3)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-38 | Fields as on Primary Records | |
  | 39 | Continuation Record Number (1) | 5.16 |
  | 40 | Application Type (1) | 5.91 |
  | 41 | Start/End Indicator (1) | 5.152 |
  | 42-52 | Start/End Date (11) | 5.153 |
  | 53-74 | Blank (Spacing) (22) | |
  | 75-78 | Route Distance (4) | 5.27 |
  | 79-123 | Reserved (Expansion) (45) | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Heliport SID/STAR/Approach Flight Planning Continuation Record (4.2.3.4)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-38 | Fields as on Primary Records | |
  | 39 | Continuation Record Number (1) | 5.16 |
  | 40-123 | Fields as on Primary Records | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>

  <details>
  <summary>13 - E - STARs (HE)</summary>
  
  ![arinc-HE](uploads/1568d744a315f092e7bf92553142e514/arinc-HE.png){width=264 height=600}

  Макет записи общий с Heliport SIDs (HD) — таблицы полей см. выше, п. 4.2.3. Отличие: Route Type в колонке 20 принимает STAR-коды (см. 5.7).
  </details>

  <details>
  <summary>13 - F - Approach Procedures(HF)</summary>
  
  ![arinc-HF](uploads/d399b411bb99ececa9d84427d6e84ad3/arinc-HF.png){width=264 height=600}

  Макет записи общий с Heliport SIDs (HD) — таблицы полей см. выше, п. 4.2.3. Отличия: Route Type в колонке 20 принимает Approach-коды, Qualifier 1/2 — в колонках 119/120 (см. 5.7); идентификатор — Approach Route Identifier (5.10); Multiple Indicator в колонке 26; DH/MDH и Procedure Category — в Continuation Record (4.2.3.2).
  </details>

  <details>
  <summary>13 - S - MSA (HS)</summary>
  
  ![arinc-HS](uploads/c254e18782b254890d3b5d94c81c969e/arinc-HS.png){width=301 height=425}

  **Heliport MSA Primary Record (4.2.4.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Blank (Spacing) (1) | |
  | 7-10 | Heliport Identifier (4) | 5.6 |
  | 11-12 | ICAO Code (2) | 5.14 |
  | 13 | Subsection Code (1) | 5.5 |
  | 14-18 | MSA Center (5) | 5.144 |
  | 19-20 | ICAO Code (2) | 5.14 |
  | 21 | Section Code (1) | 5.4 |
  | 22 | Subsection Code (1) | 5.5 |
  | 23 | Multiple Code (1) | 5.130 |
  | 24-38 | Reserved (Expansion) (15) | |
  | 39 | Continuation Record Number (1) | 5.16 |
  | 40 | Reserved (Spacing) (1) | |
  | 41-42 | Radius Limit (2) | 5.145 |
  | 43-45 | Sector Bearing (3) | 5.146 |
  | 46-48 | Sector Altitude (3) | 5.147 |
  | 49-51 | Sector Bearing (3) | 5.146 |
  | 52-54 | Sector Altitude (3) | 5.147 |
  | 55-57 | Sector Bearing (3) | 5.146 |
  | 58-60 | Sector Altitude (3) | 5.147 |
  | 61-63 | Sector Bearing (3) | 5.146 |
  | 64-66 | Sector Altitude (3) | 5.147 |
  | 67-69 | Sector Bearing (3) | 5.146 |
  | 70-72 | Sector Altitude (3) | 5.147 |
  | 73 | Magnetic/True Indicator (1) | 5.165 |
  | 74-123 | Reserved (Expansion) (50) | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Heliport MSA Continuation Record (4.2.4.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-38 | Fields as on Primary Records | |
  | 39 | Continuation Record Number (1) | 5.16 |
  | 40 | Reserved (Spacing) (1) | |
  | 41-109 | Notes (69) | 5.61 |
  | 110-123 | Reserved (Expansion) (14) [^HS1] | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  [^HS1]: В оригинале указана длина (31); 110-123 — это 14 колонок (в 4.1.20.2 — (14)).

  Примечание: колонка 40 зарезервирована под символ Application Type.
  </details>

  <details>
  <summary>13 - V - Communications (HV)</summary>
  
  ![arinc-HV](uploads/4225b1027b3dae9770a296d5849b9321/arinc-HV.png){width=327 height=576}

  **Heliport Communications Primary Record (4.2.5.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Blank (Spacing) (1) | |
  | 7-10 | Heliport Identifier (4) | 5.6 |
  | 11-12 | ICAO Code (2) | 5.14 |
  | 13 | Subsection Code (1) | 5.5 |
  | 14-16 | Communications Type (3) | 5.101 |
  | 17-23 | Communications Freq (7) | 5.103 |
  | 24 | Guard/Transmit (1) | 5.182 |
  | 25 | Frequency Units (1) | 5.104 |
  | 26 | Continuation Record No. (1) | 5.16 |
  | 27-29 | Service Indicator (3) | 5.106 |
  | 30 | Radar Service (1) | 5.102 |
  | 31 | Modulation (1) | 5.198 |
  | 32 | Signal Emission (1) | 5.199 |
  | 33-41 | Latitude (9) | 5.36 |
  | 42-51 | Longitude (10) | 5.37 |
  | 52-56 | Magnetic Variation (5) | 5.39 |
  | 57-61 | Facility Elevation (5) | 5.92 |
  | 62 | H24 Indicator (1) | 5.181 |
  | 63-68 | Sectorization (6) | 5.183 |
  | 69 | Altitude Description (1) | 5.29 |
  | 70-74 | Communication Altitude (5) | 5.184 |
  | 75-79 | Communication Altitude (5) | 5.184 |
  | 80-83 | Sector Facility (4) | 5.185 |
  | 84-85 | ICAO Code (2) | 5.14 |
  | 86 | Section Code (1) | 5.4 |
  | 87 | Subsection Code (1) | 5.5 |
  | 88 | Distance Description (1) | 5.187 |
  | 89-90 | Communications Distance (2) | 5.188 |
  | 91-94 | Remote Facility (4) [^HV1] | 5.200 |
  | 95-96 | ICAO Code (2) | 5.14 |
  | 97 | Section Code (1) | 5.4 |
  | 98 | Subsection Code (1) | 5.5 |
  | 99-123 | Call Sign (25) | 5.105 |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  [^HV1]: В оригинале «91 thru 94 Remote Facility (40)» — 91-94 это 4 колонки.

  **Heliport Communications Continuation Record (4.2.5.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-25 | Fields as on Primary Records | |
  | 26 | Continuation Record No. (1) | 5.16 |
  | 27 | Blank (Spacing) (1) | |
  | 28-87 | Narrative (60) | 5.186 |
  | 88-123 | Reserved (Expansion) (36) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Heliport Communications Continuation Record (4.2.5.3)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-25 | Fields as on Primary Records | |
  | 26 | Continuation Record No. (1) | 5.16 |
  | 27 | Blank (Spacing) (1) | |
  | 28 | Time Code (1) | 5.131 |
  | 29 | NOTAM (1) | 5.132 |
  | 30 | Time Indicator (1) | 5.138 |
  | 31-100 | 7 блоков Time of Operation (10) | 5.195 |
  | 101-123 | Reserved (Expansion) (23) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>
</details>
  


<details>
<summary>5 - P - Airport</summary>

[//]: # (6)

- 6 - Blank
- 7-10 - Region Code or Airport ICAO Identifier 
- 11-12 - ICAO Code
- 13 - Subsection Code
  <details>
  <summary>13 - A - Airport Records (PA)</summary>
  
  ![arinc-PA](uploads/6e1ba94299b4c30a6f2355a304550c80/arinc-PA.png){width=339 height=507}

  **Airport Primary Record (4.1.7.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Blank (Spacing) (1) | |
  | 7-10 | Airport ICAO Identifier (4) | 5.6 |
  | 11-12 | ICAO Code (2) | 5.14 |
  | 13 | Subsection Code (1) | 5.5 |
  | 14-16 | ATA/IATA Designator (3) | 5.107 |
  | 17-18 | Reserved (Expansion) (2) | |
  | 19-21 | Blank (Spacing) (3) | |
  | 22 | Continuation Record Number (1) | 5.16 |
  | 23-27 | Speed Limit Altitude (5) | 5.73 |
  | 28-30 | Longest Runway (3) | 5.54 |
  | 31 | IFR Capability (1) | 5.108 |
  | 32 | Longest Runway Surface Code (1) | 5.249 |
  | 33-41 | Airport Reference Pt. Latitude (9) | 5.36 |
  | 42-51 | Airport Reference Pt. Longitude (10) | 5.37 |
  | 52-56 | Magnetic Variation (5) | 5.39 |
  | 57-61 | Airport Elevation (5) | 5.55 |
  | 62-64 | Speed Limit (3) | 5.72 |
  | 65-68 | Recommended Navaid (4) | 5.23 |
  | 69-70 | ICAO Code (2) | 5.14 |
  | 71-75 | Transitions Altitude (5) | 5.53 |
  | 76-80 | Transition Level (5) | 5.53 |
  | 81 | Public/Military Indicator (1) | 5.177 |
  | 82-84 | Time Zone (3) | 5.178 |
  | 85 | Daylight Indicator (1) | 5.179 |
  | 86 | Magnetic/True Indicator (1) | 5.165 |
  | 87-89 | Datum Code (3) | 5.197 |
  | 90-93 | Reserved (Expansion) (4) | |
  | 94-123 | Airport Name (30) | 5.71 |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Airport Continuation Record (4.1.7.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Field as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23 | Reserved (Spacing) (1) | |
  | 24-92 | Notes (69) | 5.61 |
  | 93-123 | Reserved (Expansion) (31) [^PA1] | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  [^PA1]: В оригинале указана длина (59); 93-123 — это 31 колонка.

  Примечание: колонка 23 зарезервирована под символ кода приложения.

  **Airport Flight Planning Continuation Record (4.1.7.3)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23 | Application Type (1) | 5.91 |
  | 24-27 | FIR Identifier (4) | 5.116 |
  | 28-31 | UIR Identifier (4) | 5.116 |
  | 32 | Start/End Indicator (1) | 5.152 |
  | 33-43 | Start/End Date (11) | 5.153 |
  | 44-66 | Blank (Spacing) (23) | |
  | 67 | Controlled A/S Indicator (1) | 5.217 |
  | 68-71 | Controlled A/S Arpt Ident (4) | 5.6 |
  | 72-73 | Controlled A/S Arpt ICAO (2) | 5.14 |
  | 74-123 | Blank (Spacing) (50) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Airport Flight Planning Continuation Record (4.1.7.4)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23-123 | Fields as on Primary Records | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>

  <details>
  <summary>13 - B - Gates (PB)</summary>
  
  ![arinc-PB](uploads/a8683827a57f22095eb61e88327a6091/arinc-PB.png){width=322 height=250}

  **Airport Gate Primary Record (4.1.8.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Blank (Spacing) (1) | |
  | 7-10 | Airport ICAO Identifier (4) | 5.6 |
  | 11-12 | ICAO Code (2) | 5.14 |
  | 13 | Subsection Code (1) | 5.5 |
  | 14-18 | Gate Identifier (5) | 5.56 |
  | 19-21 | Blank (Spacing) (3) | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23-32 | Blank (Spacing) (10) | |
  | 33-41 | Gate Latitude (9) | 5.36 |
  | 42-51 | Gate Longitude (10) | 5.37 |
  | 52-98 | Reserved (Expansion) (47) | |
  | 99-123 | Notes (25) | 5.60 |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Airport Gate Continuation Record (4.1.8.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Field as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23 | Reserved (Spacing) (1) | |
  | 24-92 | Notes (69) | 5.61 |
  | 93-123 | Reserved (Expansion) (31) [^PB1] | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  [^PB1]: В оригинале указана длина (59); 93-123 — это 31 колонка.

  Примечание: колонка 23 зарезервирована под символ кода приложения.
  </details>

  <details>
  <summary>13 - C - Terminal Waypoints (PC)</summary>
  
  ![arinc-PC](uploads/da7b15308c37764b33f2b31554d64116/arinc-PC.png){width=326 height=405}

  Макет записи общий с Enroute Waypoints (EA) — таблицы полей см. выше, п. 4.1.4. Отличия: Subsection Code в колонке 13 (колонка 6 blank), Region Code содержит Airport ICAO Identification code.
  </details>

  <details>
  <summary>13 - D - SIDs (PD)</summary>
  
  ![arinc-PD](uploads/10415a5df1ceb2f88f84686bc5b8448e/arinc-PD.png){width=290 height=600}

  **Airport SID/STAR/Approach Primary Record (4.1.9.1)** — макет общий для PD/PE/PF

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Blank (Spacing) (1) | |
  | 7-10 | Airport Identifier (4) | 5.6 |
  | 11-12 | ICAO Code (2) | 5.14 |
  | 13 | Subsection Code (1) | 5.5 |
  | 14-19 | SID/STAR/Approach Identifier (6) | 5.9, 5.10 |
  | 20 | Route Type (1) | 5.7 |
  | 21-25 | Transition Identifier (5) | 5.11 |
  | 26 | Blank (Spacing) (1) | |
  | 27-29 | Sequence Number (3) | 5.12 |
  | 30-34 | Fix Identifier (5) | 5.13 |
  | 35-36 | ICAO Code (2) | 5.14 |
  | 37 | Section Code (1) | 5.4 |
  | 38 | Subsection Code (1) | 5.5 |
  | 39 | Continuation Number (1) | 5.16 |
  | 40-43 | Waypoint Description Code (4) | 5.17 |
  | 44 | Turn Direction (1) | 5.20 |
  | 45-47 | RNP (3) | 5.211 |
  | 48-49 | Path and Termination (2) | 5.21 |
  | 50 | Turn Direction Valid (1) | 5.22 |
  | 51-54 | Recommended Navaid (4) | 5.23 |
  | 55-56 | ICAO Code (2) | 5.14 |
  | 57-62 | ARC Radius (6) | 5.204 |
  | 63-66 | Theta (4) | 5.24 |
  | 67-70 | Rho (4) | 5.25 |
  | 71-74 | Magnetic Course (4) | 5.26 |
  | 75-78 | Route Distance/Holding Distance or Time (4) | 5.27 |
  | 79 | RECD NAV Section (1) | 5.4 |
  | 80 | RECD NAV Subsection (1) | 5.5 |
  | 81-82 | Reserved (Expansion) (2) | |
  | 83 | Altitude Description (1) | 5.29 |
  | 84 | ATC Indicator (1) | 5.81 |
  | 85-89 | Altitude (5) | 5.30 |
  | 90-94 | Altitude (5) | 5.30 |
  | 95-99 | Transition Altitude (5) | 5.53 |
  | 100-102 | Speed Limit (3) | 5.72 |
  | 103-106 | Vertical Angle (4) | 5.70 |
  | 107-111 | Center Fix (5) | 5.144 |
  | 112 | Multiple Code (1) | 5.130 |
  | 113-114 | ICAO Code (2) | 5.14 |
  | 115 | Section Code (1) | 5.4 |
  | 116 | Subsection Code (1) | 5.5 |
  | 117 | GPS/FMS Indication (1) | 5.222 |
  | 118 | Blank (Spacing) (1) | |
  | 119 | Apch Route Qualifier 1 (1) | 5.7 |
  | 120 | Apch Route Qualifier 2 (1) | 5.7 |
  | 121-123 | Blank (Spacing) (3) | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  Примечания:
  1. Для approach route idents, включающих «Multiple Indicator», см. 5.10.
  2. Колонки 119 и 120 (Apch Route Qualifier 1 и 2) требуются для сопоставления Primary Record с Continuation Record. Нестандартная сортировка выбрана, чтобы максимально сохранить Primary Record для SID/STAR/Approach Records — эти новые поля введены в Supplement 14.
  3. Для записей RNAV Procedures с несколькими минимумами значение RNP находится в колонках 90-92 Continuation Record и связано с Procedure Category. В этом случае RNP в колонках 45-47 Primary Record — blank.

  **Airport SID/STAR/Approach Continuation Record (4.1.9.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-38 | Fields as on Primary Records | |
  | 39 | Continuation Record Number (1) | 5.16 |
  | 40 | Reserved (Spacing) (1) | |
  | 41-44 | CAT A Decision Height (4) | 5.170 |
  | 45-48 | CAT B Decision Height (4) | 5.170 |
  | 49-52 | CAT C Decision Height (4) | 5.170 |
  | 53-56 | CAT D Decision Height (4) | 5.170 |
  | 57-60 | CAT A Minimum Descent Altitude (4) | 5.171 |
  | 61-64 | CAT B Minimum Descent Altitude (4) | 5.171 |
  | 65-68 | CAT C Minimum Descent Altitude (4) | 5.171 |
  | 69-72 | CAT D Minimum Descent Altitude (4) | 5.171 |
  | 73-85 | Blank Spacing (13) | |
  | 86-89 | Procedure Category (4) | 5.242 |
  | 90-92 | RNP (3) | 5.211 |
  | 93-118 | Reserved (Expansion) (26) | |
  | 119 | Apch Route Qualifier 1 (1) | 5.7 |
  | 120 | Apch Route Qualifier 2 (1) | 5.7 |
  | 121-123 | Blank (Spacing) (3) | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  Примечания:
  1. Колонка 40 зарезервирована под символ Application Type.
  2. Колонки 119 и 120 (Apch Route Qualifier 1 и 2) — часть ключа сортировки для сопоставления Continuation Record с Primary Record.
  3. Для записей RNAV Procedures с несколькими минимумами RNP в колонках 90-92 связан с Procedure Category.

  **Airport SID/STAR/Approach Flight Planning Continuation Record (4.1.9.3)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-38 | Field as on Primary | |
  | 39 | Continuation Record No. (1) | 5.16 |
  | 40 | Application Type (1) | 5.91 |
  | 41 | Start/End Indicator (1) | 5.152 |
  | 42-52 | Start/End Date (11) | 5.153 |
  | 53-74 | Blank (Spacing) (22) | |
  | 75-78 | Route Distance (4) | 5.27 |
  | 79-123 | Reserved (Expansion) (45) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Airport SID/STAR Flight Planning Continuation Record (4.1.9.4)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-38 | Fields as on Primary | |
  | 39 | Continuation Record No. (1) | 5.16 |
  | 40-123 | Fields as on Primary Records | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>

  <details>
  <summary>13 - E - STARs (PE)</summary>
  
  ![arinc-PE](uploads/7246b69f1418b9e4ec864e0fef370df9/arinc-PE.png){width=290 height=600}

  Макет записи общий с SIDs (PD) — таблицы полей см. выше, п. 4.1.9. Отличие: Route Type в колонке 20 принимает STAR-коды (см. 5.7).
  </details>

  <details>
  <summary>13 - F - Approach Procedures (PF)</summary>
  
  ![arinc-PF](uploads/5ad46c3839b7630250ddc02b0cfb7a3b/arinc-PF.png){width=290 height=600}

  Макет записи общий с SIDs (PD) — таблицы полей см. выше, п. 4.1.9. Отличия: Route Type в колонке 20 принимает Approach-коды, а Qualifier 1/2 — в колонках 119/120 (см. 5.7); идентификатор — Approach Route Identifier (5.10); Decision Height / Minimum Descent Altitude и Procedure Category — в Continuation Record (4.1.9.2).
  </details>

  <details>
  <summary>13 - G - Runways (PG)</summary>
  
  ![arinc-PG](uploads/66591b018fc70c0e6f03777810a2ddd4/arinc-PG.png){width=314 height=534}

  **Runway Primary Record (4.1.10.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Blank (Spacing) (1) | |
  | 7-10 | Airport ICAO Identifier (4) | 5.6 |
  | 11-12 | ICAO Code (2) | 5.14 |
  | 13 | Subsection Code (1) | 5.5 |
  | 14-18 | Runway Identifier (5) | 5.46 |
  | 19-21 | Blank (Spacing) (3) | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23-27 | Runway Length (5) | 5.57 |
  | 28-31 | Runway Magnetic Bearing (4) | 5.58 |
  | 32 | Blank (Spacing) (1) | |
  | 33-41 | Runway Latitude (9) | 5.36 |
  | 42-51 | Runway Longitude (10) | 5.37 |
  | 52-56 | Runway Gradient (5) | 5.212 |
  | 57-66 | Blank (Spacing) (10) | |
  | 67-71 | Landing Threshold Elevation (5) | 5.68 |
  | 72-75 | Displaced Threshold Distance (4) | 5.69 |
  | 76-77 | Threshold Crossing Height (2) | 5.67 |
  | 78-80 | Runway Width (3) | 5.109 |
  | 81 | Blank (Spacing) (1) | |
  | 82-85 | Localizer/MLS/GLS Ref Path Identifier (4) | 5.44 |
  | 86 | Localizer/MLS/GLS Category/Class (1) | 5.80 |
  | 87-90 | Stopway (4) | 5.79 |
  | 91-94 | Second Localizer/MLS/GLS Ref Path Ident (4) | 5.44 |
  | 95 | Second Localizer/MLS/GLS Category/Class (1) | 5.80 |
  | 96-101 | Reserved (Expansion) (6) | |
  | 102-123 | Runway Description (22) | 5.59 |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Runway Continuation Record (4.1.10.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23 | Reserved (Spacing) (1) | |
  | 24-92 | Notes (69) | 5.61 |
  | 93-123 | Reserved (Expansion) (31) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  Примечание: колонка 23 зарезервирована под символ кода приложения.

  **Runway Simulation Continuation Record (4.1.10.3)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23 | Application Type (1) | 5.91 |
  | 24-51 | Reserved (Spacing) (28) | |
  | 52-56 | Runway True Bearing (5) | 5.94 |
  | 57 | True Bearing Source (1) | 5.95 |
  | 58-65 | Reserved (Spacing) (8) | |
  | 66 | TDZE Location (1) | 5.98 |
  | 67-71 | Touchdown Zone Elevation (5) | 5.97 |
  | 72-123 | Reserved (Expansion) (52) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>

  <details>
  <summary>13 - I - Localizer/Glide Slope (PI)</summary>
  
  ![arinc-PI](uploads/859dfcd89b4537f91da81efe6a4e3d57/arinc-PI.png){width=339 height=401}

  **Airport and Heliport Localizer and Glide Slope Primary Record (4.1.11.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Blank (Spacing) (1) | |
  | 7-10 | Airport Identifier (4) | 5.6 |
  | 11-12 | ICAO Code (2) | 5.14 |
  | 13 | Subsection Code (1) | 5.5 |
  | 14-17 | Localizer Identifier (4) | 5.44 |
  | 18 | ILS Category (1) | 5.80 |
  | 19-21 | Blank (Spacing) (3) | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23-27 | Localizer Frequency (5) | 5.45 |
  | 28-32 | Runway Identifier (5) | 5.46 |
  | 33-41 | Localizer Latitude (9) | 5.36 |
  | 42-51 | Localizer Longitude (10) | 5.37 |
  | 52-55 | Localizer Bearing (4) | 5.47 |
  | 56-64 | Glide Slope Latitude (9) | 5.36 |
  | 65-74 | Glide Slope Longitude (10) | 5.37 |
  | 75-78 | Localizer Position (4) | 5.48 |
  | 79 | Localizer Position Reference (1) | 5.49 |
  | 80-83 | Glide Slope Position (4) | 5.50 |
  | 84-87 | Localizer Width (4) | 5.51 |
  | 88-90 | Glide Slope Angle (3) | 5.52 |
  | 91-95 | Station Declination (5) | 5.66 |
  | 96-97 | Glide Slope Height at Landing Threshold (2) | 5.67 |
  | 98-102 | Glide Slope Elevation (5) | 5.74 |
  | 103-123 | Reserved (Expansion) (21) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Airport and Heliport Localizer and Glide Slope Continuation Record (4.1.11.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23 | Reserved (Spacing) (1) | |
  | 24-92 | Notes (69) | 5.61 |
  | 93-123 | Reserved (Expansion) (31) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  Примечание: колонка 23 зарезервирована под символ кода приложения.

  **Airport and Heliport Localizer and Glide Slope Simulation Continuation Record (4.1.11.3)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Fields as on Primary Record | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23 | Application Type (1) | 5.91 |
  | 24-27 | Blank (Spacing) (4) | |
  | 28-32 | Facility Characteristics (5) | 5.93 |
  | 33-51 | Blank (Spacing) (19) | |
  | 52-56 | Localizer True Bearing (5) | 5.94 |
  | 57 | Localizer Bearing Source (1) | 5.95 |
  | 58-87 | Reserved (Spacing) (30) | |
  | 88-90 | Glide Slope Beam Width (3) | 5.96 |
  | 91-96 | Approach Route Ident (6) | 5.10 |
  | 97-102 | Approach Route Ident (6) | 5.10 |
  | 103-108 | Approach Route Ident (6) | 5.10 |
  | 109-114 | Approach Route Ident (6) | 5.10 |
  | 115-120 | Approach Route Ident (6) | 5.10 |
  | 121-123 | Blank (Spacing) (3) [^PI1] | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  [^PI1]: В оригинале «120 thru 123 Blank (spacing) (4)»; 120-я колонка занята пятым Approach Route Ident — корректно 121-123 (3).
  </details>

  <details>
  <summary>13 - L - MLS (PL)</summary>
  
  ![arinc-PL](uploads/409ff345fe850f3270eb187bfb9bbdb2/arinc-PL.png){width=323 height=529}

  **Airport and Heliport MLS Primary Record (4.1.22.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Blank (Spacing) (1) | |
  | 7-10 | Airport Identifier (4) | 5.6 |
  | 11-12 | ICAO Code (2) | 5.14 |
  | 13 | Subsection Code (1) | 5.5 |
  | 14-17 | MLS Identifier (4) | 5.44 |
  | 18 | MLS Category (1) | 5.80 |
  | 19-21 | Blank (Spacing) (3) | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23-25 | Channel (3) | 5.166 |
  | 26-27 | Blank (Spacing) (2) | |
  | 28-32 | Runway Identifier (5) | 5.46 |
  | 33-41 | Azimuth Latitude (9) | 5.36 |
  | 42-51 | Azimuth Longitude (10) | 5.37 |
  | 52-55 | Azimuth Bearing (4) | 5.167 |
  | 56-64 | Elevation Latitude (9) | 5.36 |
  | 65-74 | Elevation Longitude (10) | 5.37 |
  | 75-78 | Azimuth Position (4) | 5.48 |
  | 79 | Azimuth Position Reference (1) | 5.49 |
  | 80-83 | Elevation Position (4) | 5.50 |
  | 84-86 | Azimuth Proportional Angle Right (3) | 5.168 |
  | 87-89 | Azimuth Proportional Angle Left (3) | 5.168 |
  | 90-92 | Azimuth Coverage Right (3) | 5.172 |
  | 93-95 | Azimuth Coverage Left (3) | 5.172 |
  | 96-98 | Elevation Angle Span (3) | 5.169 |
  | 99-103 | Magnetic Variation (5) | 5.39 |
  | 104-108 | EL Elevation (5) | 5.74 |
  | 109-112 | Nominal Elevation Angle (4) | 5.173 |
  | 113-115 | Minimum Glide Path Angle (3) | 5.52 |
  | 116-123 | Reserved (Expansion) (8) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Airport and Heliport MLS Continuation Record (4.1.22.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-21 | Field as on Primary Records | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23-27 | Blank (Spacing) (5) | |
  | 28-32 | Facility Characteristics (5) | 5.93 |
  | 33-41 | Back Azimuth Latitude (9) | 5.36 |
  | 42-51 | Back Azimuth Longitude (10) | 5.37 |
  | 52-55 | Back Azimuth Bearing (4) | 5.167 |
  | 56-64 | MLS Datum Point Latitude (9) | 5.36 |
  | 65-74 | MLS Datum Point Longitude (10) | 5.37 |
  | 75-78 | Back Azimuth Position (4) | 5.48 |
  | 79 | Back Azimuth Position Reference (1) | 5.49 |
  | 80-83 | Blank (Spacing) (4) | |
  | 84-86 | Back Azimuth Proportional Sector Right (3) | 5.168 |
  | 87-89 | Back Azimuth Proportional Sector Left (3) | 5.168 |
  | 90-92 | Back Azimuth Coverage Right (3) | 5.172 |
  | 93-95 | Back Azimuth Coverage Left (3) | 5.172 |
  | 96-100 | Back Azimuth True Bearing (5) | 5.94 |
  | 101 | Back Azimuth Bearing Source (1) | 5.95 |
  | 102-106 | Azimuth True Bearing (5) | 5.94 |
  | 107 | Azimuth Bearing Source (1) | 5.95 |
  | 108-109 | Glide Path Height at Landing Threshold (2) | 5.67 |
  | 110-123 | Reserved (Expansion) (14) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>

  <details>
  <summary>13 - M - Localizer Marker (PM)</summary>
  
  ![arinc-PM](uploads/d00915fe16cf4ff9e5e7195f5bd49559/arinc-PM.png){width=333 height=436}

  **Airport and Heliport Localizer Primary Record (4.1.13.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Blank (Spacing) (1) | |
  | 7-10 | Airport Identifier (4) | 5.6 |
  | 11-12 | ICAO Code (2) | 5.14 |
  | 13 | Subsection Code (1) | 5.5 |
  | 14-17 | Localizer Identifier (4) | 5.44 |
  | 18-20 | Marker Type (3) | 5.99 |
  | 21 | Blank (Spacing) (1) | |
  | 22 | Continuation Record No. (1) | 5.16 |
  | 23-27 | Locator Frequency (5) | 5.34 |
  | 28-32 | Runway Identifier (5) | 5.46 |
  | 33-41 | Marker Latitude (9) | 5.36 |
  | 42-51 | Marker Longitude (10) | 5.37 |
  | 52-55 | Minor Axis Bearing (4) | 5.100 |
  | 56-64 | Locator Latitude (9) | 5.36 |
  | 65-74 | Locator Longitude (10) | 5.37 |
  | 75-79 | Locator Class (5) | 5.35 |
  | 80-84 | Locator Facility Characteristics (5) | 5.93 |
  | 85-88 | Locator Identifier (4) | 5.33 |
  | 89-90 | Blank (Spacing) (2) | |
  | 91-95 | Magnetic Variation (5) | 5.39 |
  | 96-97 | Blank (Spacing) (2) | |
  | 98-102 | Facility Elevation (5) | 5.92 |
  | 103-123 | Reserved (Expansion) (21) [^PM1] | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  [^PM1]: В оригинале указана длина (31); 103-123 — это 21 колонка.
  </details>

  <details>
  <summary>13 - N - Terminal NDB (PN)</summary>
  
  Макет записи общий с NDB NAVAID (DB) — таблицы полей см. выше, п. 4.1.3. Отличие: Terminal NDB NAVAID file (PN) содержит NDB, связанные с аэропортами подраздела 3.2.4.1 и вертодромами раздела 3.3.3.
  </details>

  <details>
  <summary>13 - P - Pathpoint (PP)</summary>
  
  ![arinc-PP](uploads/5f7ccb838e1d95fb7dbe52bffec152aa/arinc-PP.png){width=322 height=564}

  **Path Point Primary Record (4.1.28.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Blank (Spacing) (1) | |
  | 7-10 | *Airport Identifier (4) | 5.6 |
  | 11-12 | ICAO Code (2) | 5.14 |
  | 13 | Subsection Code (1) | 5.5 |
  | 14-19 | *Approach Identifier (6) | 5.10 |
  | 20-24 | *Runway or Helipad Identifier (5) | 5.46 или 5.180 |
  | 25-26 | *Operation Type (2) | 5.223 |
  | 27 | *Approach Indicator (1) | 5.224 |
  | 28-38 | Blank (Spacing) (11) | |
  | 39 | Continuation Number (1) | 5.16 |
  | 40-48 | *Landing Threshold Point Latitude (9) | 5.36 |
  | 49-58 | *Landing Threshold Point Longitude (10) | 5.37 |
  | 59-64 | *(LTP) WGS-84 Ellipsoid Height (6) | 5.225 |
  | 65-66 | *(FPCP) Threshold Crossing Height (2) | 5.67 |
  | 67 | Blank (1) | |
  | 68-71 | *Glide Path Angle (4) | 5.226 |
  | 72-80 | *Flight Path Alignment Point Latitude (9) [^PP1] | 5.36 |
  | 81-90 | *Flight Path Alignment Point Longitude (10) | 5.37 |
  | 91-96 | (FPAP) WGS-84 Ellipsoid Height (6) | 5.225 |
  | 97-102 | (FPAP) Orthometric Height (6) | 5.227 |
  | 103-108 | (FPCP) Orthometric Height (6) | 5.227 |
  | 109 | *Unit of Height (1) | 5.228 |
  | 110-115 | Blank (Spacing) (6) | |
  | 116-123 | Path Point Data CRC (8) | 5.229 |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  [^PP1]: В оригинале «72 thru 80 ... Latitude (10)» — 72-80 это 9 колонок.

  Примечание источника: концепция pathpoint находится в разработке FAA; многие поля ещё не финализированы — соблюдать осторожность при создании ПО.
  </details>

  <details>
  <summary>13 - R - Fit Planning ARR/DEP (PR)</summary>
  
  ![arinc-PR](uploads/d6f10c811d8f76692c415dfcd2397bde/arinc-PR.png){width=257 height=600}

  **Primary Record (4.1.27.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Blank (Spacing) (1) | |
  | 7-10 | Airport Identifier (4) | 5.6 |
  | 11-12 | ICAO Code (2) | 5.14 |
  | 13 | Subsection Code (1) | 5.5 |
  | 14-19 | SID/STAR/Approach Identifier (6) | 5.9, 5.10 |
  | 20 | Procedure Type (1) | 5.230 |
  | 21-25 | Runway Transition Identifier (5) | 5.11 |
  | 26-30 | Runway Transition Fix (5) | 5.13 |
  | 31-32 | ICAO Code (2) | 5.14 |
  | 33 | Section Code (1) | 5.4 |
  | 34 | Subsection Code (1) | 5.5 |
  | 35-37 | Runway Transition Along Track Distance (3) | 5.231 |
  | 38-42 | Common Segment Transition Fix (5) | 5.13 |
  | 43-44 | ICAO Code (2) | 5.14 |
  | 45 | Section Code (1) | 5.4 |
  | 46 | Subsection Code (1) | 5.5 |
  | 47-49 | Common Segment Along Track Distance (3) | 5.231 |
  | 50-54 | Enroute Transition Identifier (5) | 5.11 |
  | 55-59 | Enroute Transition Fix (5) | 5.13 |
  | 60-61 | ICAO Code (2) | 5.14 |
  | 62 | Section Code (1) | 5.4 |
  | 63 | Subsection Code (1) | 5.5 |
  | 64-66 | Enroute Transition Along Track Distance (3) | 5.231 |
  | 67-69 | Sequence Number (3) | 5.12 |
  | 70 | Continuation Number (1) | 5.16 |
  | 71-74 | Number of Engines (4) | 5.232 |
  | 75 | Turboprop/Jet Indicator (1) | 5.233 |
  | 76 | RNAV Flag (1) | 5.234 |
  | 77 | ATC Weight Category (1) | 5.235 |
  | 78-84 | ATC Identifier (7) | 5.236 |
  | 85 | Time Code (1) | 5.131 |
  | 86-100 | Procedure Description (15) | 5.237 |
  | 101-102 | Leg Type Code (2) | 5.238 |
  | 103 | Reporting Code (1) | 5.239 |
  | 104-107 | Initial Departure Magnetic Course (4) | 5.26 |
  | 108 | Altitude Description (1) | 5.29 |
  | 109-111 | Altitude (3) | 5.240 |
  | 112-114 | Altitude (3) | 5.240 |
  | 115-117 | Speed Limit (3) | 5.72 |
  | 118-119 | Initial Cruise Table (2) | 5.134 |
  | 120-123 | Blank (Spacing) (4) | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Continuation Record (4.1.27.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-69 | Fields as on Primary Records | |
  | 70 | Continuation Number (1) | 5.16 |
  | 71 | Application Number (1) | 5.91 |
  | 72-123 | 4 группы: Intermediate Fix Identifier (5) 5.13 → ICAO Code (2) 5.14 → Section Code (1) 5.4 → Subsection Code (1) 5.5 → Intermediate Distance (3) 5.231 → Fix Related Transition Code (1) 5.241 | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Continuation Record (4.1.27.3)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-69 | Fields as on Primary Records | |
  | 70 | Continuation Number (1) | 5.16 |
  | 71 | Application Type (1) | 5.91 |
  | 72 | Time Code (1) | 5.131 |
  | 73 | Time Indicator (1) | 5.138 |
  | 74-123 | 5 блоков Time of Operation (10) | 5.195 |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  Примечание: запись 4.1.27.4 несёт Time of Operation в «note»-форме, начиная с колонки 74 и до колонки 123, где требуется.
  </details>

  <details>
  <summary>13 - S - MSA (PS)</summary>
  
  ![arinc-PS](uploads/e88006782cde026fc9ab3fcfc01a4e54/arinc-PS.png){width=333 height=462}

  **Airport MSA Primary Record (4.1.20.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Blank (Spacing) (1) | |
  | 7-10 | Airport Identifier (4) | 5.6 |
  | 11-12 | ICAO Code (2) | 5.14 |
  | 13 | Subsection Code (1) | 5.5 |
  | 14-18 | MSA Center (5) | 5.144 |
  | 19-20 | ICAO Code (2) | 5.14 |
  | 21 | Section Code (1) | 5.4 |
  | 22 | Subsection Code (1) | 5.5 |
  | 23 | Multiple Code (1) | 5.130 |
  | 24-38 | Reserved (Expansion) (15) | |
  | 39 | Continuation Record No. (1) | 5.16 |
  | 40 | Reserved (Spacing) (1) | |
  | 41-42 | Radius Limit (2) | 5.145 |
  | 43-45 | Sector Bearing (3) | 5.146 |
  | 46-48 | Sector Altitude (3) | 5.147 |
  | 49-51 | Sector Bearing (3) | 5.146 |
  | 52-54 | Sector Altitude (3) | 5.147 |
  | 55-57 | Sector Bearing (3) | 5.146 |
  | 58-60 | Sector Altitude (3) | 5.147 |
  | 61-63 | Sector Bearing (3) | 5.146 |
  | 64-66 | Sector Altitude (3) | 5.147 |
  | 67-69 | Sector Bearing (3) | 5.146 |
  | 70-72 | Sector Altitude (3) | 5.147 |
  | 73 | Magnetic/True Ind (1) | 5.165 |
  | 74-123 | Reserved (Expansion) (50) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Airport MSA Continuation Record (4.1.20.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-38 | Field as on Primary Records | |
  | 39 | Continuation Record No. (1) | 5.16 |
  | 40 | Reserved (Spacing) (1) | |
  | 41-109 | Notes (69) | 5.61 |
  | 110-123 | Reserved (Expansion) (14) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>

  <details>
  <summary>13 - T - GLS Station (PT)</summary>
  
  ![arinc-PT](uploads/1a57939381aeee7e0fc03167da72bbdc/arinc-PT.png){width=326 height=489}

  **GLS Primary Record (4.1.29.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Blank (1) | |
  | 7-10 | Airport or Heliport Identifier (4) | 5.6 |
  | 11-12 | ICAO Code (2) | 5.14 |
  | 13 | Subsection Code (1) | 5.5 |
  | 14-17 | GLS Ref Path Identifier (4) | 5.44 |
  | 18 | GLS Category (1) | 5.80 |
  | 19-21 | Blank (3) | |
  | 22 | Continuation Number (1) | 5.16 |
  | 23-27 | GLS Channel (5) | 5.244 |
  | 28-32 | Runway Identifier (5) | 5.46 |
  | 33-51 | Blank (19) | |
  | 52-55 | GLS Approach Bearing (4) [^PT1] | 5.47 |
  | 56-64 | Station Latitude (9) | 5.36 |
  | 65-74 | Station Longitude (10) | 5.37 |
  | 75-78 | GLS Station ident (4) | 5.243 |
  | 79-83 | Blank (5) | |
  | 84-85 | Service Volume Radius (2) | 5.245 |
  | 86-87 | TDMA Slots (2) | 5.246 |
  | 88-90 | GLS Approach Slope (3) | 5.52 |
  | 91-95 | Magnetic Variation (5) | 5.39 |
  | 96-97 | Reserved (2) | |
  | 98-102 | Station Elevation (5) | 5.74 |
  | 103-105 | Datum Code (3) | 5.197 |
  | 106-108 | Station Type (3) | 5.247 |
  | 109-110 | Blank (2) [^PT2] | |
  | 111-115 | Station Elevation WGS84 (5) | 5.248 |
  | 116-123 | Blank (8) | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  [^PT1]: GLS reference point должен совпадать с IFR landing threshold position — это точка отсчёта траектории.
  [^PT2]: В оригинале «109 thru 110 Blank (3)» — 109-110 это 2 колонки.

  Примечание: все широты/долготы записи относятся к одному datum code.
  </details>

  <details>
  <summary>13 - V - Communications (PV)</summary>
  
  ![arinc-PV](uploads/26e2b899dd26ea21bf9a069b094a4f80/arinc-PV.png){width=321 height=523}

  **Airport Communications Primary Record (4.1.14.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Blank (Spacing) (1) | |
  | 7-10 | Airport Identifier (4) | 5.6 |
  | 11-12 | ICAO Code (2) | 5.14 |
  | 13 | Subsection Code (1) | 5.5 |
  | 14-16 | Communications Type (3) | 5.101 |
  | 17-23 | Communications Freq (7) | 5.103 |
  | 24 | Guard/Transmit (1) | 5.182 |
  | 25 | Frequency Units (1) | 5.104 |
  | 26 | Continuation Record No. (1) | 5.16 |
  | 27-29 | Service Indicator (3) | 5.106 |
  | 30 | Radar Service (1) | 5.102 |
  | 31 | Modulation (1) | 5.198 |
  | 32 | Signal Emission (1) | 5.199 |
  | 33-41 | Latitude (9) | 5.36 |
  | 42-51 | Longitude (10) | 5.37 |
  | 52-56 | Magnetic Variation (5) | 5.39 |
  | 57-61 | Facility Elevation (5) | 5.92 |
  | 62 | H24 Indicator (1) | 5.181 |
  | 63-68 | Sectorization (6) | 5.183 |
  | 69 | Altitude Description (1) | 5.29 |
  | 70-74 | Communication Altitude (5) | 5.184 |
  | 75-79 | Communication Altitude (5) | 5.184 |
  | 80-83 | Sector Facility (4) | 5.185 |
  | 84-85 | ICAO Code (2) | 5.14 |
  | 86 | Section Code (1) | 5.4 |
  | 87 | Subsection Code (1) | 5.5 |
  | 88 | Distance Description (1) | 5.187 |
  | 89-90 | Communications Distance (2) | 5.188 |
  | 91-94 | Remote Facility (4) | 5.200 |
  | 95-96 | ICAO Code (2) | 5.14 |
  | 97 | Section Code (1) | 5.4 |
  | 98 | Subsection Code (1) | 5.5 |
  | 99-123 | Call Sign (25) | 5.105 |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Airport Communications Continuation Record (4.1.14.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-25 | Fields as on Primary Records | |
  | 26 | Continuation Record No. (1) | 5.16 |
  | 27 | Reserved Spacing (1) | |
  | 28-87 | Narrative (60) | 5.186 |
  | 88-123 | Reserved (Expansion) (36) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Airport Additional Continuation Record (4.1.14.3)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-25 | Fields as on Primary Records | |
  | 26 | Continuation Record No. (1) | 5.16 |
  | 27 | Blank (Spacing) (1) | |
  | 28 | Time Code (1) | 5.131 |
  | 29 | NOTAM (1) | 5.132 |
  | 30 | Time Indicator (1) | 5.138 |
  | 31-40 | Time of Operation (10) | 5.195 |
  | 41-50 | Time of Operation (10) | 5.195 |
  | 51-60 | Time of Operation (10) | 5.195 |
  | 61-70 | Time of Operation (10) | 5.195 |
  | 71-80 | Time of Operation (10) | 5.195 |
  | 81-90 | Time of Operation (10) | 5.195 |
  | 91-100 | Time of Operation (10) | 5.195 |
  | 101-123 | Reserved (Expansion) (23) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>
</details>
  


<details>
<summary>5 - R - Company Routes</summary>
  
[//]: # (6)

- 6 - Subsection Code (SUB CODE)
  <details>
  <summary>6 - Blank - Company Routes (R)</summary>
  
  ![arinc-RBlank](uploads/14b3ce8161f3bde7d3fc76a9a340b5c1/arinc-RBlank.png){width=324 height=459}

  **Company Primary Record (4.1.12.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Subsection Code (1) | 5.5 |
  | 7-11 | From Airport/Fix (5) | 5.75 |
  | 12 | Blank (Spacing) (1) | |
  | 13-14 | ICAO Code (2) | 5.14 |
  | 15 | Section Code (1) | 5.4 |
  | 16 | Subsection Code (1) | 5.5 |
  | 17-21 | To Airport/Fix (5) | 5.75 |
  | 22 | Blank (Spacing) (1) | |
  | 23-24 | ICAO Code (2) | 5.14 |
  | 25 | Section Code (1) | 5.4 |
  | 26 | Subsection Code (1) | 5.5 |
  | 27-36 | Company Route ID (10) | 5.76 |
  | 37-39 | Sequence No. (3) | 5.12 |
  | 40-42 | Via (3) | 5.77 |
  | 43-48 | SID/STAR/App/Awy (6) | 5.78 |
  | 49-51 | Area Code (3) | 5.3 |
  | 52-57 | To Fix (6) | 5.83 |
  | 58-59 | ICAO Code (2) | 5.14 |
  | 60 | Section Code (1) | 5.4 |
  | 61 | Subsection Code (1) | 5.5 |
  | 62-66 | Runway Trans (5) | 5.84 |
  | 67-71 | ENRT Trans (5) | 5.85 |
  | 72 | Reserved (1) | |
  | 73-77 | Cruise Altitude (5) | 5.86 |
  | 78-81 | Terminal/Alternate Airport (4) | 5.87 |
  | 82-83 | ICAO Code (2) | 5.14 |
  | 84-87 | Alternate Distance (4) | 5.88 |
  | 88-90 | Cost Index (3) | 5.89 |
  | 91-94 | Enroute Alternate Airport (4) | 5.148 |
  | 95-123 | Reserved (Expansion) (29) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>

  <details>
  <summary>6 - A - Alternate Records (RA)</summary>
  
  ![arinc-RA](uploads/e078790a24ccfee71b9ea4657a7ef665/arinc-RA.png){width=343 height=549}

  **Alternate Primary Record (4.1.30.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Subsection Code (1) | 5.5 |
  | 7-11 | Alternate Related Airport or Fix (5) | 5.75 |
  | 12-13 | Alternate Related ICAO Code (2) | 5.14 |
  | 14 | Alternate Related Section Code (1) | 5.4 |
  | 15 | Alternate Related Subsection Code (1) | 5.5 |
  | 16-17 | Alternate Record Type (2) | 5.250 |
  | 18-19 | Blank (Spacing) (2) | |
  | 20-22 | Distance to Alternate (3) | 5.251 |
  | 23 | Alternate Type (1) | 5.252 |
  | 24-33 | Primary Alternate Identifier (10) | 5.253 |
  | 34-35 | Blank (Spacing) (2) | |
  | 36-38 | Distance to Alternate (3) | 5.251 |
  | 39 | Alternate Type (1) | 5.252 |
  | 40-49 | Additional Alternate Identifier One (10) | 5.253 |
  | 50-51 | Blank (Spacing) (2) | |
  | 52-54 | Distance to Alternate (3) | 5.251 |
  | 55 | Alternate Type (1) | 5.252 |
  | 56-65 | Additional Alternate Identifier Two (10) | 5.253 |
  | 66-67 | Blank (Spacing) (2) | |
  | 68-70 | Distance to Alternate (3) | 5.251 |
  | 71 | Alternate Type (1) | 5.252 |
  | 72-81 | Additional Alternate Identifier Three (10) | 5.253 |
  | 82-83 | Blank (Spacing) (2) | |
  | 84-86 | Distance to Alternate (3) | 5.251 |
  | 87 | Alternate Type (1) | 5.252 |
  | 88-97 | Additional Alternate Identifier Four (10) | 5.253 |
  | 98-99 | Blank (Spacing) (2) | |
  | 100-102 | Distance to Alternate (3) | 5.251 |
  | 103 | Alternate Type (1) | 5.252 |
  | 104-113 | Additional Alternate Identifier Five (10) | 5.253 |
  | 114-123 | Reserved (Expansion) (10) | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>
</details>
  


<details>
<summary>5 - T - Tables</summary>
  
[//]: # (6)

- 6 - Subsection Code (SUB CODE)
  <details>
  <summary>6 - C - Cruising Tables (TC)</summary>
  
  ![arinc-TC](uploads/3e46927fef83c5bcffe565c7b560ac1d/arinc-TC.png){width=315 height=327}

  **Cruising Table Primary Record (4.1.16.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Blank (Spacing) (3) | |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Subsection Code (1) | 5.5 |
  | 7-8 | Cruise Table Identifier (2) | 5.134 |
  | 9 | Sequence Number (1) | 5.12 |
  | 10-28 | Blank (Spacing) (19) | |
  | 29-32 | Course From (4) | 5.135 |
  | 33-36 | Course To (4) | 5.135 |
  | 37 | Mag/True (1) | 5.165 |
  | 38-39 | Blank (Spacing) (2) | |
  | 40-44 | Cruise Level From (5) | 5.136 |
  | 45-49 | Vertical Separation (5) | 5.137 |
  | 50-54 | Cruise Level To (5) | 5.136 |
  | 55-99 | 3 группы: Cruise Level From (5) 5.136 → Vertical Separation (5) 5.137 → Cruise Level To (5) 5.136 | |
  | 100-123 | Reserved (Expansion) (24) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>

  <details>
  <summary>6 - G - Geographical Reference (TG)</summary>
  
  ![arinc-TG](uploads/b15353ee7d382e9a36dcce56c0f035b6/arinc-TG.png){width=334 height=380}

  **Geographical Reference Table Primary Record (4.1.26.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Subsection Code (1) | 5.5 |
  | 7-8 | Geographical Ref Table ID (2) | 5.218 |
  | 9 | Sequence Number (1) | 5.12 |
  | 10-38 | Geographical Entity (29) | 5.219 |
  | 39 | Continuation Record No (1) | 5.16 |
  | 40 | Reserved (1) | |
  | 41-112 | 6 групп: Preferred Route Ident (10) 5.8 → Preferred Route Use Ind (2) 5.220 | |
  | 113-123 | Blank (Spacing) (11) | |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>
</details>
  

<details>
<summary>5 - U - Airspace</summary>
  
[//]: # (6)

- 6 - Subsection Code (SUB CODE)
  <details>
  <summary>6 - C - Controlled Airspace (UC)</summary>
  
  ![arinc-UC](uploads/f374f73507baa4f918976b863111fbab/arinc-UC.png){width=341 height=506}

  **Controlled Airspace Primary Record (4.1.25.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Subsection Code (1) | 5.5 |
  | 7-8 | ICAO Code (2) | 5.14 |
  | 9 | Airspace Type (1) | 5.213 |
  | 10-14 | Airspace Center (5) | 5.214 |
  | 15 | Section Code (1) | 5.4 |
  | 16 | Subsection Code (1) | 5.5 |
  | 17 | Airspace Classification (1) | 5.215 |
  | 18-19 | Reserved (Spacing) (2) | |
  | 20 | Multiple Code (1) | 5.130 |
  | 21-24 | Sequence Number (4) | 5.12 |
  | 25 | Continuation Record Number (1) | 5.16 |
  | 26 | Level (1) | 5.19 |
  | 27 | Time Code (1) | 5.131 |
  | 28 | NOTAM (1) | 5.132 |
  | 29-30 | Blank (Spacing) (2) | |
  | 31-32 | Boundary Via (2) | 5.118 |
  | 33-41 | Latitude (9) | 5.36 |
  | 42-51 | Longitude (10) | 5.37 |
  | 52-60 | Arc Origin Latitude (9) | 5.36 |
  | 61-70 | Arc Origin Longitude (10) | 5.37 |
  | 71-74 | Arc Distance (4) | 5.119 |
  | 75-78 | Arc Bearing (4) | 5.120 |
  | 79-81 | RNP (3) | 5.211 |
  | 82-86 | Lower Limit (5) | 5.121 |
  | 87 | Unit Indicator (1) | 5.133 |
  | 88-92 | Upper Limit (5) | 5.121 |
  | 93 | Unit Indicator (1) | 5.133 |
  | 94-123 | Controlled Airspace Name (30) | 5.216 |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Controlled Airspace Continuation Record (4.1.25.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-24 | Fields as on Primary Records | |
  | 25 | Continuation Record Number (1) | 5.16 |
  | 26 | Time Code (1) | 5.131 |
  | 27 | NOTAM (1) | 5.132 |
  | 28 | Time Indicator (1) | 5.138 |
  | 29-98 | 7 блоков Time of Operations (10) | 5.195 |
  | 99-123 | Controlling Agency (25) | 5.140 |
  | 124-128 | File Record Number (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>

  <details>
  <summary>6 - F - FIR/UIR (UF)</summary>
  
  ![arinc-UF](uploads/d609b58777d357508919981184a1892a/arinc-UF.png){width=321 height=372}

  **FIR/UIR Primary Record (4.1.17.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Subsection Code (1) | 5.5 |
  | 7-10 | FIR/UIR Identifier (4) | 5.116 |
  | 11-14 | FIR/UIR Address (4) | 5.151 |
  | 15 | FIR/UIR Indicator (1) | 5.117 |
  | 16-19 | Sequence Number (4) | 5.12 |
  | 20 | Continuation Record No. (1) | 5.16 |
  | 21-24 | Adjacent FIR Identifier (4) | 5.116 |
  | 25-28 | Adjacent UIR Identifier (4) | 5.116 |
  | 29 | Reporting Units Speed (1) | 5.122 |
  | 30 | Reporting Units Altitude (1) | 5.123 |
  | 31 | Entry Report (1) | 5.124 |
  | 32 | Blank (Spacing) (1) | |
  | 33-34 | Boundary Via (2) | 5.118 |
  | 35-43 | FIR/UIR Latitude (9) | 5.36 |
  | 44-53 | FIR/UIR Longitude (10) | 5.37 |
  | 54-62 | Arc Origin Latitude (9) | 5.36 |
  | 63-72 | Arc Origin Longitude (10) | 5.37 |
  | 73-76 | Arc Distance (4) | 5.119 |
  | 77-80 | Arc Bearing (4) | 5.120 |
  | 81-85 | FIR Upper Limit (5) | 5.121 |
  | 86-90 | UIR Lower Limit (5) | 5.121 |
  | 91-95 | UIR Upper Limit (5) | 5.121 |
  | 96-97 | Cruise Table Ind (2) | 5.134 |
  | 98 | Reserved (Expansion) (1) | |
  | 99-123 | FIR/UIR Name (25) | 5.125 |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>

  <details>
  <summary>6 - R - Restrictive Airspace (UR)</summary>
  
  ![arinc-UR](uploads/a7a12cac76670214a170d1ad7f3b4a14/arinc-UR.png){width=321 height=357}

  **Restrictive Airspace Primary Record (4.1.18.1)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1 | Record Type (1) | 5.2 |
  | 2-4 | Customer/Area Code (3) | 5.3 |
  | 5 | Section Code (1) | 5.4 |
  | 6 | Subsection Code (1) | 5.5 |
  | 7-8 | ICAO Code (2) | 5.14 |
  | 9 | Restrictive Type (1) | 5.128 |
  | 10-19 | Restrictive Airspace Designation (10) | 5.129 |
  | 20 | Multiple Code (1) | 5.130 |
  | 21-24 | Sequence Number (4) | 5.12 |
  | 25 | Continuation Record No. (1) | 5.16 |
  | 26 | Level (1) | 5.19 |
  | 27 | Time Code (1) | 5.131 |
  | 28 | NOTAM (1) | 5.132 |
  | 29-30 | Blank (Spacing) (2) | |
  | 31-32 | Boundary Via (2) | 5.118 |
  | 33-41 | Latitude (9) | 5.36 |
  | 42-51 | Longitude (10) | 5.37 |
  | 52-60 | Arc Origin Latitude (9) | 5.36 |
  | 61-70 | Arc Origin Longitude (10) | 5.37 |
  | 71-74 | Arc Distance (4) | 5.119 |
  | 75-78 | Arc Bearing (4) | 5.120 |
  | 79-81 | Blank (Spacing) (3) | |
  | 82-86 | Lower Limit (5) | 5.121 |
  | 87-92 | Upper Limit (5) | 5.121 |
  | 93 | Unit Indicator (1) | 5.133 |
  | 94-123 | Restrictive Airspace Name (30) | 5.126 |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Restrictive Airspace Continuation Record (4.1.18.2)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-24 | Fields as on Primary Records | |
  | 25 | Continuation Record No. (1) | 5.16 |
  | 26 | Time Code (1) | 5.131 |
  | 27 | NOTAM (1) | 5.132 |
  | 28 | Time Indicator (1) | 5.138 |
  | 29-98 | 7 блоков Time of Operation (10) | 5.195 |
  | 99-123 | Controlling Agency (25) | 5.140 |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |

  **Restrictive Airspace Flight Planning Continuation Record (4.1.18.3)**

  | Колонки | Поле (длина) | Ссылка |
  |---|---:|---|
  | 1-24 | Fields as on Primary Records | |
  | 25 | Continuation Record No. (1) | 5.16 |
  | 26-29 | Blank (Spacing) (4) | |
  | 30 | Start/End Indicator (1) | 5.152 |
  | 31-41 | Start/End Date (11) | 5.153 |
  | 42-123 | Reserved (Expansion) (82) | |
  | 124-128 | File Record No. (5) | 5.31 |
  | 129-132 | Cycle Date (4) | 5.32 |
  </details>
</details>

<br>


**T - Tailored (included on the master tape for a single user’s specific purpose)**

1 - Tailored

2-4 Airlines for whom tailored records are provided in the master file

Airline codes should be derived from the standard list of abbreviated identifiers maintained and published in the IATA Airline Coding Directory

## 5.0 NAVIGATION DATA - FIELD DEFINITIONS (глава 5)

<details>
<summary>5 - Field Definitions (глава 5)</summary>

<details>
<summary>5.1 - General</summary>

Chapter 5 sets forth definitions/descriptions and content for each type of field employed in the records discussed in Chapter 4. The following information is presented for each field:

(i) Field Name (paragraph heading)
(ii) Abbreviation used in proportional record layouts (Chapter 4) when different than Field Name (follows paragraph heading)
(iii) Field Definition/Description
(iv) Source/Content of each field
(v) Length of field, expressed in number of characters
(vi) Type of character allowed in each field, alpha or numeric or alpha/numeric
(vii) Examples of field content when appropriate and/or necessary

The following general rules apply to the format of all the fields:

(i) All numeric fields, and the numeric parts of latitude, longitude, magnetic variation, negative elevation and station declination fields will be right justified and filled with leading zeros.
(ii) All alpha and alpha/numeric fields will be left justified.
(iii) Allowable field content of blank is defined as alpha/numeric content.
</details>

<details>
<summary>5.2 - Record Type (S/T)</summary>

**Definition/Description:** The "Record Type" field content indicates whether the record data are "standard," i.e., suitable for universal application, or "tailored," i.e. included on the master tape for a single user's specific purpose. (Section 1.2 of this Specification refers.)

**Source/Content:** The field contains the letter "S" when the field data are "standard" and the letter "T" when they are "tailored."

**Used On:** All records
**Length:** One character
**Character Type:** Alpha
</details>

<details>
<summary>5.3 - Customer/Area Code (CUST/AREA)</summary>

**Definition/Description:** The "Customer Area Code" field permits the categorization of standard records by geographical area and of tailored records by the airlines for whom they are provided in the master file. Several record types do not adhere to the established geographical boundaries. There is no "AREA" in such records.

**Source/Content:** "AREA" Codes should be derived from Figure 5-2. Airline codes should be derived from the standard list of abbreviated identifiers maintained and published in the IATA Airline Coding Directory. On Company Route and Preferred Route Records, an additional AREA field is used as a pointer to the AREA in which the Route Segment is located. For records, which do not follow geographical boundaries, the field is blank. For Preferred Routes, the field content is "PDR".

**Used On:** All records with content as defined above.
**Length:** 3 characters max
**Character Type:** Alpha
**Examples:** Areas - USA, CAN, EUR / Customer - UAL, DAL, TWA / Preferred Routes - PDR
</details>

<details>
<summary>5.4 - Section Code (SEC CODE)</summary>

**Definition/Description:** The "Section Code" field defines the major section of the navigation system data base in which the record resides.

**Source/Content:** Figure 5-1 shows the data base section encoding scheme.

**Used On:** All records
**Length:** One character
**Character Type:** Alpha
</details>

<details>
<summary>5.5 - Subsection Code (SUB CODE)</summary>

**Definition/Description:** The "Subsection Code" field defines the specific part of the database major section in which the record resides.

Additionally, records that reference other records within the database use Section/Subsection Codes to make the reference, together with the record identifier. This is true for "fix" information in Holdings, Enroute Airways, Airport and Heliport SID/STAR/APPROACH, all kinds of Communications, Airport and Heliport MSA, Company Routes, Enroute Airway Restrictions, Preferred Routes and Alternate Records. The Section Code will define the major section, the Subsection Code permits the exact section (file) to be identified and the "fix" (record) can then be located within this file.

**Source/Content:** Figure 5-1 shows the database Subsection Encoding Scheme.

| Section Code | Section Name | Subsection Code | Subsection Name |
|---|---|---|---|
| A | MORA | S | Grid MORA |
| D | Navaid | Blank | VHF Navaid |
| | | B | NDB Navaid |
| E | Enroute | A | Waypoints |
| | | M | Airway Markers |
| | | P | Holding Patterns |
| | | R | Airways and Routes |
| | | T | Preferred Routes |
| | | U | Airway Restrictions |
| | | V | Communications |
| H | Heliport | A | Pads |
| | | C | Terminal Waypoints |
| | | D | SIDs |
| | | E | STARs |
| | | F | Approach Procedures |
| | | S | MSA |
| | | V | Communications |
| P | Airport | A | Reference Points |
| | | B | Gates |
| | | C | Terminal Waypoints |
| | | D | SIDs |
| | | E | STARs |
| | | F | Approach Procedures |
| | | G | Runways |
| | | I | Localizer/Glide Slope |
| | | L | MLS |
| | | M | Localizer Marker |
| | | N | Terminal NDB |
| | | P | Pathpoint |
| | | R | Flt Planning ARR/DEP |
| | | S | MSA |
| | | T | GLS Station |
| | | V | Communications |
| R | Company Routes | Blank | Company Routes |
| | | A | Alternate Records |
| T | Tables | C | Cruising Tables |
| | | G | Geographical Reference |
| U | Airspace | C | Controlled Airspace |
| | | F | FIR/UIR |
| | | R | Restrictive Airspace |

**Used On:** All records
**Length:** One character
**Character Type:** Alpha
</details>

<details>
<summary>5.6 - Airport/Heliport Identifier (ARPT/HELI IDENT)</summary>

**Definition/Description:** The "Airport Identifier" and the "Heliport Identifier" fields contain the identification of the airport or heliport to which the data contained in the record relates.

**Source/Content:** The content of this field is derived from official government sources. It will be the four character ICAO Location Identifier of the airport or heliport when such is published. It will be the three or four character Domestic Identifier when published and no ICAO Location Identifier is available for the airport or heliport. When used on Airport or Heliport Flight Planning Continuation Records, it will be the Airport or Heliport Identifier owning the terminal controlled airspace referenced in that record.

Note: Within the continental United States and within Canada, in addition to using the published four character ICAO Location Identifier, a "K" for the USA or a "C" for Canada may be appended to certain Domestic Identifiers to present an ICAO look-alike four character identifier.

COMMENTARY: Where no officially published identifier is available, a data supplier may create a unique, temporary and unofficial identifier. Airports or Heliports within such identifiers may supply Tailored Data only and with full knowledge and concurrence of the data user. Whenever possible, such temporary identifiers should be coordinated among the various data suppliers prior to its release.

The content of this Airport/Heliport Identifier should not be confused with the perhaps more familiar ATA/IATA two or three character identifiers often used by airlines for other than navigation purposes. These ATA/IATA identifiers are included in the ARINC 424 database in accordance with Section 5.107 of this Specification.

**Used On:** Airport Identifier - VHF Navaid, NDB Navaid, Airport Terminal Waypoint, Airport, Airport Gate, Airport SID/STAR/Approach, Runway, Airport and Heliport Localizer, Airport and Heliport Localizer Marker, Holding Pattern, Airport Communications, Airport and Heliport MLS, GLS Airport MSA, Path Point Flight Planning Arrival Departure Data and GLS Record. Heliport Identifier - VHF Navaid, NDB Navaid, Heliport Terminal Waypoint, Heliport, Heliport SID/STAR/Approach, Airport and Heliport Localizer, Airport and Heliport Localizer Marker, Holding Pattern, Heliport Communications, Airport and Heliport MLS, GLS Heliport MSA, Path Point Flight Planning Arrival/Departure Data and GLS Records.
**Length:** 4 characters maximum
**Character Type:** Alpha/numeric
**Examples:** KJFK, DMIA, 9Y9, CYUL, EDDF, 53Y, CA14
</details>

<details>
<summary>5.7 - Route Type (RT TYPE)</summary>

**Definition/Description:** The "Route Type" field defines the type of Enroute Airway, Preferred Route, Airport and Heliport SID/STAR/Approach Routes of which the record is an element. For Airport and Heliport Approach Routes, "Route Type" includes a "primary route type," and up to two "route type qualifiers."

**Source/Content:** The content of this field will be as indicated in the following tables:

Enroute Airway Records (ER):

| Airway Type | Field Content |
|---|---|
| Airline Airway (Tailored Data) | A |
| Control | C |
| Direct Route | D |
| Helicopter Airways | H |
| Officially Designated Airways, except RNAV, Helicopter Airways | O |
| RNAV Airways | R |
| Undesignated ATS Route | S |

Preferred Route Records (ET):

| Route Type Description | Field Content |
|---|---|
| North American Routes for North Atlantic Traffic | C |
| Common Portion | D |
| Preferential Routes | J |
| Pacific Oceanic Transition Routes (PACOSTS) | M |
| North American Routes for North Atlantic Traffic – Non-common Portion | N |
| Preferred/Preferential Overflight Routes | 0 |
| Preferred Routes | P |
| Traffic Orientation System Routes (TOS) | S |
| Tower Enroute Control Routes (TEC) | T |

Airport SID (PD) and Heliport SID (HD) Records:

| SID Route Type Description | Field Content |
|---|---|
| Engine Out SID | 0 |
| SID Runway Transition | 1 |
| SID or SID Common Route | 2 |
| SID Enroute Transition | 3 |
| RNAV SID Runway Transition | 4 |
| RNAV SID or SID Common Route | 5 |
| RNAV SID Enroute Transition | 6 |
| FMS SID Runway Transition | F |
| FMS SID or SID Common Route | M |
| FMS SID Enroute Transition | S |
| Vector SID Runway Transition | T |
| Vector SID Enroute Transition | V |

Airport STAR (PE) and Heliport STAR (HE) Records:

| STAR Route Type Description | Field Content |
|---|---|
| STAR Enroute Transition | 1 |
| STAR or STAR Common Route | 2 |
| STAR Runway Transition | 3 |
| RNAV STAR Enroute Transition | 4 |
| RNAV STAR or STAR Common Route | 5 |
| RNAV STAR Runway Transition | 6 |
| Profile Descent Enroute Transition | 7 |
| Profile Descent Common Route | 8 |
| Profile Descent Runway Transition | 9 |
| FMS STAR Enroute Transition | F |
| FMS STAR or STAR Common Route | M |
| FMS STAR Runway Transition | S |

Airport Approach (PF) and Heliport Approach (HF) Records (Route Type + Qualifier 1 Field + Qualifier 2 Field):

| Approach Route Type Description | Route Type Field Content | Qualifier 1 Field Content | Qualifier 2 Field Content |
|---|---|---|---|
| Approach Transition | A | | |
| Localizer/Backcourse Approach | B | | |
| RNAV, GPS Required Approach | E | | |
| Flight Management System (FMS) Approach | F | | |
| Instrument Guidance System (IGS) Approach | G | | |
| Instrument Landing System (ILS) Approach | I | | |
| LAAS-GPS/GLS Approach | J | | |
| WAAS-GPS Approach | K | | |
| Localizer Only (LOC) Approach | L | | |
| Microwave Landing System (MLS) Approach | M | | |
| Non-Directional Beacon (NDB) Approach | N | | |
| Global Positioning System (GPS) Approach | P | | |
| Area Navigation (RNAV) Approach (Note 1) | R | | |
| TACAN Approach | T | | |
| Simplified Directional Facility (SDF) Approach | U | | |
| VOR Approach | V | | |
| Microwave Landing System (MLS), Type A Approach | W | | |
| Localizer Directional Aid (LDA) Approach | X | | |
| Microwave Landing System (MLS), Type B and C Approach | Y | | |
| Missed Approach | Z | | |
| DME Required for Procedure | | D | |
| DME Not Required for Procedure | | N | |
| DME/DME Required for Procedure | | T | |
| Primary Missed Approach | | | P |
| Secondary Missed Approach | | | S |
| Procedure with Circle-To-Land Minimums | | | C |
| Procedure with Straight-in Minimums | | | S |
| Procedure Designed for Helicopter to Runway | | | H |

The listing above for Approach Route Type is alphabetical and does not represent any kind of priority.

Note 1: Conventional Area Navigation Approach using RHO-RHO or RHO-THETA equipment.

Note 2: Path Point Data Records are required to support these Approach Procedure Types.

Note 3: The Qualifiers 1 (values "D," "N," and "T") and 2 (all values) can be used in conjunction with any Route Type except for "A" and "Z". Qualifier 1 values "P" and "S" can be used only in conjunction with Route Type "Z".

Note 4: The content of this Route Type is split in the record layout. The Primary Route Type is in column 20 and the Qualifiers 1 and 2 in columns 119 and 120. Only the Primary Route Type is used to sort the file content.

Note 5: Approach Procedures designed for helicopter operations to helipads, previously designated with a Route Type of "H," are now identified by Route Types in this table and the fact that they are provided as "HF" records. Procedures designed for helicopter operations to runways use the Route Types in this Table and the "H" in Qualifier 2.

**Used On:** Enroute Airways, Airport and Heliport SID/STAR/Approach, Preferred Route
**Length:** One for Enroute Airways, Airport and Heliport SID and STAR and Preferred Routes. Three for Airport and Heliport Approach Procedures
**Character Type:** Alpha/Numeric
**Examples:** LDC = a Localizer-based procedure, for localizer only, no glide slope, with DME required, Circle-To-Land Minimums; V S = A VOR procedure, using VORDME or VORTAC Navaid, DME not required, Straight-in Minimums; VDS = A VOR procedure DME required straight-in minimums.
</details>

<details>
<summary>5.8 - Route Identifier (ROUTE IDENT)</summary>

**Definition/Description:** The "Route Identifier" field identifies a route of flight or traffic orientation, using the coding employed on aeronautical navigation charts and related publications.

**Source/Content:** For Enroute Airways, Route Identifier codes should be derived from official government publications. For Preferred Routes, Route Identifiers may or may not be provided in government publications. Where they are available, they will be used.

For North American Routes for North Atlantic Traffic, "Common Portion" and other similar route system, route identifier code shall be those published in government sources. For the European Traffic Orientation System or other similar route systems such as North American Routes for North Atlantic Traffic, "Non-common Portion," Preferred Routes and Preferential Routes published without official and/or flight plan identifiers, but published as between specific airports or other navigation fixes, route identifiers define the initial fix and the terminus fix idents according to the naming rules in Chapter 7. For routings which do not include a unique initial or terminus fix, rules on creating unique Route Identifiers are also contained in Chapter 7. Those rules have been developed with use of the Geographical Reference Tables (TG). Refer to Chapter 3, Section 3.2.7.2 and Chapter 4, Section 4.1.26 for more detail.

**Used On:** Enroute Airway, Preferred Route Records and Geographical Reference Table
**Length:** Enroute Airway - 5 character maximum; Preferred Route - 10 character maximum
**Character Type:** Alpha/Numeric
**Examples:** Enroute Airway - V216, C1150, J380, UA16, UB414; Preferred Routes - N111B, TOS13, TOS14WK, CYYLCYYC, ARTCOLAR, KZTLKSAV, SCNDICANRY

Refer to Section 7 for specific examples and their meaning.
</details>

<details>
<summary>5.9 - SID/STAR Route Identifier (SID/STAR IDENT)</summary>

**Definition/Description:** "The SID/STAR Route Identifier" field contains the name of the SID or STAR, using the basic indicator, validity indicator and route indicator and abbreviated to six characters with the naming rules in Chapter 7 of this document.

**Source/Content:** SID/STAR route identifier codes should be derived from official government publications describing the terminal procedures structure.

**Used On:** Airport SID/STAR, Heliport SID/STAR and Flight Planning Arrival/Departure Data Records
**Length:** 6 characters max
**Character Type:** Alpha/numeric
**Examples:** DEPU2, SCK4, TRP7, 41M3, MONTH6
</details>

<details>
<summary>5.10 - Approach Route Identifier (APPROACH IDENT)</summary>

**Definition/Description:** The "Approach Route Identifier" field contains the identifier of the approach route to be flown. To facilitate the provision of multiple approach procedures of the same type to a given runway, the field also is used to provide a "multiple indicator."

**Source/Content:** For approach procedures coded to a specific runway for airport approaches, the first position of the identifier will carry a character indicating the type of approach. The second through fourth characters will carry the runway identification and the fifth character will carry the multiple indicator, where appropriate. For approach procedures coded with only circle-to-land minimums and not runway dependent, allow a four character alpha identifier. The fifth character will carry the multiple indicator on airport approaches, where appropriate. Other identifiers may be used for circle-to-land approach procedures, applying as much of the source ident as possible. To ensure that any possible multiple indicator is always located in the fifth position of the identifier, the fourth position may contain a dash (-) when the runway designation being used does not include a Left, Right, Center or True indication.

For Helicopter Approach Procedure to Runways, the first position of the identifier will be the type of approach. The second through fourth positions will carry a three digit numeric representing the procedure final approach course, expressed in full degrees. Where the same final approach course is used multiple times in official source, the fifth position will carry a multiple indicator.

For Helicopter Approach Procedures to Heliports and coded to a specific pad, the first position of the identifier will carry a character indicating the type of approach. The second through sixth characters will carry the pad identification. There is no provision for a multiple indicator for more than one approach of the same type to the same pad in this identifier field. When required, a multiple indicator is provided in a separate field.

**Used On:** Airport and Heliport Approach Route Records, Flight Planning Arrival/Departure Data, Path Point and Airport, Heliport Localizer Simulation Continuation Records.
**Length:** 6 characters max.
**Character Type:** Alpha/Numeric
**Examples:** Runway Dependent: I26L, B08R, R29, V01L, N35, L16RA, L16RB, V08-A, V08-B; Circle-To-Land: VORA, NDBB, CVOR, VDMA, LOCD, CVORA, CVORB, I18L1, I18L2; Helicopter to Runway: L040, V175, N175B; Helicopter to Helipad: IA127, VBRAVO, N23, RWESTA
</details>

<details>
<summary>5.11 - Transition Identifier (TRANS IDENT)</summary>

**Definition/Description:** The "Transition Identifier" field describes the type of transition to be made from the enroute environment into the terminal area and vice versa, and from the terminal area to the approach or from the runway or helipad to the terminal area.

**Source Content:** The content of the transition identifier field should be determined from the content of the Route Type field (See Section 5.7) in accordance with the rules set forth in Figure 5.3.

Figure 5-3 (Transition Identifier Field Content):

| Route Type | Field Content |
|---|---|
| Engine Out SID | 0 | Runway (RWY) or Pad Identifier |
| SID/RNAV | 1 or 4 | Runway (RWY) or Pad Identifier |
| SID | 2 or 5 | Blank/RWY/PAD/ALL (see Notes 1 and 3) |
| SID | 3 or 6 | SID Enroute Transition Identifier |
| FMS SID | F | Runway (RWY) or Pad Identifier |
| FMS SID | M | Blank/RWY/PAD/All (see Notes 1 and 3) |
| FMS SID | S | FMS SID Enroute Transition Identifier |
| Vector SID | T | Runway (RWY) or Pad Identifier |
| Vector SID | V | Vector SID Enroute Transition Identifier |
| STAR/RNAV | 1 or 4 | STAR Enroute Transition Identifier |
| STAR | 2 or 5 | RWY/PAD/ALL/Blank (see Note 3) |
| STAR | 3 or 6 | Runway (RWY) or Pad Identifier (Note 2) |
| Profile Descent | 7 | Profile Descent Enroute Transition Ident |
| Profile Descent | 8 | RWY/PAD/ALL/Blank (see Note 3) |
| Profile Descent | 9 | Runway (RWY) or Pad Identifier (Note 2) |
| FMS STAR | F | FMS STAR Enroute Transition Identifier |
| FMS STAR | M | RWY/PAD/ALL/Blank (See Note 3) |
| FMS STAR | S | Runway (RWY) or Pad Identifier (Note 2) |
| Approach Transitions | A | Approach Transition Identifier |
| Missed Approach | Z | Missed Approach Transition Identifier (Note 4) |
| All Other Approach Procedure Codes | Blank | (see Section 5.7) |

Note 1: If there is no Route Type 1 or 4 or F for the SID, then the SID records with the Route Type of 2 or 5 or M will have an entry in the Transition Identifier field. If there is a Route Type of 1 or 4 or F for the procedure, then the records with the Route Type of 2 or 5 or M will carry a blank transition identifier field.

Note 2: If there is no Route Type 3 or 6 or 9 or S for the STAR, then the STAR record with the Route Type of 2 or 5 or 8 or M will have an entry in the Transition Identifier field. If there is a Route Type 3 or 6 or 9 or S for the procedure, then the Transition Identifier in the Route Type 2 or 5 or 8 or M will carry a blank transition identifier field.

Note 3: The use of "ALL" in the Transition Identifier field indicates that the procedure is valid for two or more runways at an airport or all helipads at a heliport. The use of the character "B" along with a runway designation such as RW08B in the Transition Identifier field indicates that the transition is valid for two or more parallel runways, e.g. RW08L and RW08R.

Note 4: The Missed Approach Transition Identifier will be the identifier of the Missed Approach Holding Fix or the last fix in the missed approach path if there is no holding fix. If multiple missed approach paths are published to the same termination but with different paths or constraints, a transition identifier closely aligned with the published source indication for each missed approach will be used. Enroute Transition Identifiers are normally the identifier of a navaid or waypoint. Transition Identifiers should be derived from official government sources, where provided.

**Used On:** Airport and Heliport SID/STAR/Approach, Flight Planning Arrival/Departure Data and Company Route Records
**Length:** 5 characters max.
**Character Type:** Alpha/numeric
**Examples:** 9TU, ETX, KEENE, DEN, RW08R, Blank
</details>

<details>
<summary>5.12 - Sequence Number (SEQ NR)</summary>

**Definition/Description:** For Route Type Records - A route of flight is defined by a series of records taken in order. The "Sequence Number" field defines the location of the record in the sequence defining the route of flight identified in the route identifier field. For Boundary Type Records - A boundary is defined by a series of records taken in order. The "Sequence Number" field defines the location of the record in the sequence defining a boundary. For Record Types requiring more than one primary record to define the complete content - In a series of primary records used to define a complete condition, the "Sequence Number" is used to define each primary record in sequence.

**Source/Content:** Sequence numbers are assigned during the route, boundary or sequence definition phase of the data file assembly. Sequence numbers are assigned so as not to be duplicated within the route, boundary or sequence assigned a unique identification/designation. For three or four digit Sequence Numbers, initially, an increment of ten should be maintained between the sequence numbers assigned to consecutive records. For one or two digit Sequence Numbers, the initial increment is one. In route or boundary records, should subsequent maintenance of the file necessitate the addition of a record or records, the new record(s) should be located in the correct position in the sequence and assigned a sequence number whose most significant characters are identical to those in the sequence number of the preceding record in sequence. The unit character should be assigned a value midway between the units character values of the preceding and following record sequence numbers. For example, if it is desired to add one record to the sequence and the units characters of the preceding and following records at the desired location are zeros (indicating no previous modification at this point), the units character of the inserted record's sequence number should be five (5). For records taken in sequence with one or two digit sequence numbers, additional data must be entered in the proper sequence and all subsequent records will be up numbered accordingly.

When an enroute airway crosses the boundary separating two geographical areas (Section 5.3), the airway fix lying on or closest to the boundary shall be coded twice, once for each geographical area, and should be assigned the same sequence number in each case. Record uniqueness in such cases is maintained through the "Boundary Code" (Section 5.18). Enroute airway record sequence numbers should be assigned in a manner which permits them to be arranged into continuous airway routes in flight sequence order when sorted according to the Route Identifier and Sequence Number only, without regard to their applicable Geographical Area Code.

**Used On:** Enroute Airways, Airport and Heliport SID/STAR/Approach, Company Route, Cruise Tables, FIR/UIR, Restrictive Airspace, Controlled Airspace, Preferred Routes, Flight Planning Arrival/Departure Data and VHF Navaid Limitation Continuation Records
**Length:** 4 characters - Enroute Airways, Preferred Routes, FIR/UIR and Restrictive Airspace; 3 characters - SID/STAR/Approach and Company Routes; 2 characters - VHF Navaid Limitation Continuation Records; 1 character - Cruise Table
**Character Type:** Numeric
**Examples:** 0010, 0135, 2076, 120, 030, 01, 84, 3
</details>

<details>
<summary>5.13 - Fix Identifier (FIX IDENT)</summary>

**Definition/Description:** The "Fix Identifier" field contains the five-character-name-code, or other series of characters, with which the fix is identified. This includes Waypoint Identifiers, VHF NAVAID Identifiers, NDB NAVAID identifier, Airport Identifiers, and Runway Identifiers.

**Source/Content:** Officially published identifiers or identifiers derived in accordance with Chapter 7, Naming Conventions, of this document.

**Used On:** Holding Patterns, Enroute Airways, Airport and Heliport SID/STAR/Approach, Enroute Airway Restrictions, and Enroute Waypoints, Airport and Heliport Terminal Waypoints (Waypoint Ident) and Flight Planning Arrival/Departure Data Records.
**Length:** 5 characters max
**Character Type:** Alpha/numeric (no embedded blanks)
**Examples:** SHARP, DEN43, BHM, RW27L, KGRR
</details>

<details>
<summary>5.14 - ICAO Code (ICAO CODE)</summary>

**Definition/Description:** The "ICAO Code" field permits records to be categorized geographically within the limits of the categorization performed by the "Area Code" field.

**Source/Content:** The code to be employed in the ICAO Code field may be found in ICAO Document No. 7910, "Location Indicators."

In order to permit sub-division of the United States into more easily manageable regions, the ICAO code for the USA (K) is followed by a numeric character obtained from Figure 5-5.

**Used On:** All records except Cruising Tables and Grid MORA
**Length:** 2 characters max
**Character Type:** Alpha/numeric
**Examples:** K1, K7, PA, MM, EG, UT
</details>

<details>
<summary>5.16 - Continuation Record Number (CONT NR)</summary>

**Definition/Description:** When it is not possible to store all the information needed on a record within the 132 columns of the record itself, the so-called Primary Record; one or more continuation records may be used. The "Continuation Record Number" identifies the position of a continuation record in a sequence of such records.

**Source/Content:** Primary records contain the numeric "0" when no Continuation Records are included in the file for that Primary. The numeric "1" in this field of the Primary Record indicates that one or more Continuation Records follow the Primary Record. Continuation Records are numbered sequentially starting with the numeric "2" in the first continuation. If the information requirement goes beyond a Continuation Record with the numeric "9," the sequence is continued with alpha characters, starting with "A" and continuing through to "Z" as required.

**Used On:** All records except Company Route, Airport Localizer Marker/Locator, Enroute Markers, Cruising Tables, FIR/UIR and Grid MORA
**Length:** One character
**Character Type:** Alpha/Numeric
**Examples:** 0, 1, 2 (through 9) A, B, C (through Z)
</details>

<details>
<summary>5.17 - Waypoint Description Code (DESC CODE)</summary>

**Definition/Description:** Fixes are located at positions significant to navigation in the Enroute, Terminal Area and Approach Procedure path definitions. The "Waypoint Description Code" field enables that significance or function of a fix at a specific location in a route to be identified. The field provides information on the type of fix. As a single fix can be used in different route structures and multiple times within a given structure, the field provides the function for each occurrence of a fix.

**Source/Content:** Valid contents for the "Waypoint Description Code" are contained in the table below (Figure 5-4). The contents of Column 40 provide information on the fix type. Column 41 is used to define whether the fix is a "fly-over" or "fly-by" fix and to indicate the charting status of some waypoints. Columns 42 and 43 provide the fix function information. Column 40, Code "G," is valid for Runway as Waypoint and Helipad as Waypoint.

Коды Column 40 (тип фикса):

| Code | Waypoint Description Type/Function | Used On |
|---|---|---|
| A | Airport as Waypoint | STAR, APCH |
| E | Essential Waypoint¹ | Enroute, SID, STAR, APCH |
| F | Off Airway Waypoint² | Enroute |
| G | Runway as Waypoint, Helipad as Waypoint | SID, STAR, APCH |
| H | Heliport as Waypoint | STAR, APCH |
| N | NDB Navaid as Waypoint | Enroute, SID, STAR, APCH |
| P | Phantom Waypoint³ | SID, STAR, APCH |
| R | Non-Essential Waypoint⁴ | Enroute |
| T | Transition Essential Waypoint⁵ | Enroute |
| V | VHF Navaid As Waypoint | Enroute, SID, STAR, APCH |

Column 41 (fly-over/fly-by):

| Code | Описание |
|---|---|
| B | Flyover Waypoint, End of SID, STAR Route Type, APCH Transition or Final Approach⁶ |
| E | End of Enroute Airway or Terminal Procedure Route Type |
| U | Uncharted Airway Intersection⁷ |
| Y | Fly-Over Waypoint⁸ |

Коды Column 42/43 (функция фикса):

| Code | Waypoint Description Type/Function | Used On |
|---|---|---|
| A | Unnamed Stepdown Fix After Final Approach Fix²⁰ | APCH |
| B | Unnamed Stepdown Fix Before Final Approach Fix²⁰ | APCH |
| C | ATC Compulsory Waypoint⁹ | Enroute |
| G | Oceanic Gateway Waypoint¹⁰ | Enroute |
| M | First Leg of Missed Approach Procedure¹¹ | APCH |
| P | Path Point Fix¹⁹ | APCH |
| S | Named Stepdown Fix¹⁸ | APCH |
| A | Initial Approach Fix¹² | APCH |
| B | Intermediate Approach Fix¹³ | APCH |
| C | Initial Approach Fix with Holding | APCH |
| D | Initial Approach Fix with Final Approach Course Fix | APCH |
| E | Final End Point Fix¹⁶ | APCH |
| F | Published Final Approach Fix or Database Final Approach Fix¹⁴ | APCH |
| H | Enroute Holding Fix | Enroute, SID, STAR, APCH |
| I | Final Approach Course Fix¹⁵ | APCH |
| M | Published Missed Approach Point Fix¹⁷ | APCH |

Explanation of superscript notes and other detail required to understand this table:

1. Any waypoint (not Navaid, Airport or Runway) in Terminal Procedures or any waypoint (not Navaid) in Enroute Airways, required for navigation such as a change in bearing, intersection of two airways, beginning or end of continuous segment. See also Special Navigation Terms in Section 2.
2. Any waypoint published by government source but not part of any route structure.
3. A waypoint established during procedure coding on the nominal track.
4. Any waypoint (not Navaid) on Enroute Airway that is not considered "Essential" or "Transition Essential." See also Special Navigation Terms in Section 2.
5. Any waypoint (not Navaid) on Enroute Airway for the purpose of transitioning between the Enroute and Terminal structures. See also Special Navigation Terms in Section 2.
6. Any waypoint (including Navaid) at the end of a SID or STAR Route Type, but not the final fix of the procedure, that must be overflown before establishing on the first leg of the following Route Type; at the end of an Approach Transition for FMS, GPS or MLS/RNAV approach prior to establishing on the final approach; any missed approach waypoint that is to be overflown during execution of the missed approach.
7. Any waypoint (not Navaid) on Enroute Airway that has not been established by government source. Used only in conjunction with "E" in Column 40.
8. Any waypoint (including Navaid) that must be overflown before establishing on the following leg.
9. Any waypoint (including Navaid) on Enroute Airway at which a "position report" must be made to the appropriate Air Traffic Control unit. See also Special Navigation Terms in Section 2.
10. Any waypoint (including Navaid) designated as the start/end of an oceanic organized track system. See also Special Navigation Terms in Section 2.
11. Coded on the first leg after a runway fix or missed approach point fix dependent on approach procedure coding rules in Attachment 5. The leg may be the first leg of a published missed approach procedure or a leg to the published missed approach point.
12. Any waypoint (including Navaid) established as an Initial Approach Fix. See also Special Navigation Terms in Section 2.
</details>

<details>
<summary>5.18 - Boundary Code (BDY CODE)</summary>

**Definition/Description:** Routes of flight frequently cross geographical boundaries. The "Boundary Code" field identifies the area from, or into which a continuous route passes when such a crossing occurs.

**Source/Content:** See Table 5-6.

Table 5-6 - Boundary Codes (Area | Area Code* | Boundary Code):

| Area | Area Code* | Boundary Code |
|---|---|---|
| USA | K | U |
| Canada and Alaska | CAN | C |
| Pacific | PAC | P |
| Latin America | LAM | L |
| South America | SAM | S |
| South Pacific | SPA | 1 |
| Europe | EUR | E |
| Eastern Europe | EEU | 2 |
| Middle East-South Asia | MES | M |
| Africa | AFR | A |

\* From Figure 5-2

**Used On:** Enroute Airways records
**Length:** One character
**Character Type:** Alpha/numeric
</details>

<details>
<summary>5.19 - Level (LEVEL)</summary>

**Definition/Description:** The Level field defines the airway structure of which the record is an element.

**Source/Content:**

| Code | Описание |
|---|---|
| B | All Altitudes |
| H | High Level Airways |
| L | Low Level Airways |

**Used On:** Enroute Airway, Preferred Routes, Restrictive Airspace, and Controlled Airspace records
**Length:** One character
**Character Type:** Alpha
</details>

<details>
<summary>5.20 - Turn Direction (TURN DIR)</summary>

**Definition/Description:** The "Turn Direction" field specifies the direction in which Terminal Procedure turns are to be made. It is also used to indicate direction on course reversals, see Attachment 5 Path and Termination.

**Source/Content:** The field contains the alpha character "L" for Left turns, "R" for Right turns and "E" for turns in either direction.

**Used On:** Airport and Heliport SID/STAR/Approach records
**Length:** One character
**Character Type:** Alpha
</details>

<details>
<summary>5.21 - Path and Termination (PATH TERM)</summary>

**Definition/Description:** The Path and Termination defines the path geometry for a single record of an ATC terminal procedure.

**Source/Content:** Attachment 5 to this document, "Path and Terminator," contains the various Path Term codes available for coding an ATC terminal procedure.

**Used On:** Airport and Heliport SID/STAR/Approach records
**Length:** 2 characters
**Character Type:** Alpha
</details>

<details>
<summary>5.22 - Turn Direction Valid (TDV)</summary>

**Definition/Description:** This field is used in conjunction with Turn direction to indicate that a turn is required prior to capturing the path defined in a terminal procedure.

**Source/Content:** The field contains the alpha character "Y" when a turn is required prior to beginning the leg defined by the Path Term. The direction of the turn is specified in the Turn direction (5-20).

**Used On:** Airport and Heliport SID/STAR/Approach Records
**Length:** One character
**Character Type:** Alpha
</details>

<details>
<summary>5.23 - Recommended NAVAID (RECD NAV)</summary>

**Definition/Description:** The "Recommended Navaid" field allows the reference facility for the waypoint in a given record "Fix Ident" field or for an Airport or Heliport to be specified. VHF, NDB (Enroute and Terminal), Localizer, GLS and MLS Navaids may be referenced.

**Source/Content:** The 1, 2, 3 or 4 character identification of the Navaid appears in this field. Navaids recommended for waypoint reference in official government publications will be used when available. The following general rules on field content apply:

a. A "VHF Navaid" may be any VOR, DME, VORDME, VORTAC, TACAN or Un-Biased ILSDME available in the database.
b. A "NDB Navaid" may be any NDB or Locator (Terminal NDB) available in the database.
c. Localizers, GLS Reference Path, and MLS Azimuth are used as Recommended Navaid for procedures that reference those navaids.
d. The Recommended Navaid in final approach procedure coding will be the procedure reference facility (when Recommended Navaid is provided in coding).
e. The Recommended Navaid in Airport and Heliport Records will be any VOR, VORDME or VORTAC available in the database.
f. The Recommended Navaid in any Enroute Airway Record will be any VORDME or VORTAC available in the database.
g. The Recommended Navaid in any Terminal Procedure Record other than the final approach coding will be the procedure reference facility of a type from the Definition/Description paragraph above and will be in accordance with the rules governing Recommended Navaids for Path Terminators and coding rule as defined in Attachment 5 of this Specification.
h. The rules for Recommended Navaids for Converging ILS Approach Procedures are the same as for ILS Approach Procedures.
i. The Recommended Navaid used in a GLS Approach Procedure will be the GLS Ref Path identifier appropriate to the runway and approach.

**Used On:** Enroute Airway Record, Airport and Heliport SID/STAR/Approach Records, Airport and Heliport Record
**Length:** 4 characters max.
**Character Type:** Alpha/Numeric
**Examples:** P, PP, DEN, LAX, ILAX, MJFK
</details>

<details>
<summary>5.24 - Theta (THETA)</summary>

**Definition/Description:** "Theta" is defined as the magnetic bearing to the waypoint identified in the record's "FIX Ident" field from the Navaid in the "Recommended Navaid" field.

**Source/Content:** Theta values are derived from official government sources when available. They are provided in degrees and tenths of a degree, with the decimal point suppressed. The content is controlled through requirements of the Path Terminator and coding rules contained in Attachment 5 of this specification.

**Used On:** Airport and Heliport SID/STAR/Approach, Enroute Airway Records
**Length:** 4 characters
**Character Type:** Alpha/numeric
**Examples:** 0000, 0756, 1217, 1800
</details>

<details>
<summary>5.25 - Rho (RHO)</summary>

**Definition/Description:** "RHO" is defined as the geodesic distance in nautical miles to the waypoint identified in the record's "Fix Ident" field from the NAVAID in the "Recommended NAVAID" field.

**Source/Content:** Rho values derived from official government sources will be used when available. They are entered into the field in nautical miles and tenths of a nautical mile, with the decimal point suppressed. The content is controlled through requirements of the Path Terminator and coding rules contained in Attachment 5 of this specification.

**Used On:** Airport and Heliport SID/STAR/Approach, Enroute Airway Records
**Length:** 4 characters
**Character Type:** Alpha/numeric
**Examples:** 0000, 0216, 0142, 1074
</details>

<details>
<summary>5.26 - Outbound Magnetic Course (OB MAG CRS)</summary>

**Definition/Description:** "Outbound Magnetic Course" is the published outbound magnetic course from the waypoint identified in the record's "Fix Ident" field. In addition, this field is used for Course/Heading/Radials on SID/STAR Approach Records through requirements of the Path Terminator and coding rules contained in Attachment 5 of this specification.

**Source/Content:** Values from official government sources will be used when available. The field contains magnetic information expressed in degrees and tenths of a degree, with the decimal point suppressed. For route and procedure segments charted in "degrees true," the last character (tenths position) of the field will contain the character "T". See also Section 5.165 of this document for more information on "degrees true" information.

**Used On:** Airport and Heliport SID/STAR/Approach, Enroute Airway and Flight Planning Arrival/Departure Data Records
**Length:** 4 characters
**Character Type:** Alpha/numeric
**Examples:** 2760, 0231, 194T
</details>

<details>
<summary>5.27 - Route Distance From, Holding Distance/Time (RTE DIST FROM, HOLD DIST/TIME)</summary>

**Definition/Description:** In Enroute Airways, "Route Distance From" is the distance in nautical miles from the waypoint identified in the records "Fix Ident" field to the next waypoint of the route. In SID, STAR and Approach Procedure records, the field may contain segment distances/along track distances/excursion distances/DME distances. The actual content is dependent on the Path and Termination. For more information on the content, refer to Table Three, Leg Data Fields, in Attachment 5 of this document.

**Source/Content:** The field contains distances, from official government source where available, expressed in nautical miles and tenths of nautical miles with the decimal point suppressed. For Holding Pattern Records and/or Path and Terminations defining holdings patterns, content may be "holding time" expressed in minutes and tenths of minutes preceded by the character "T" with the decimal point suppressed.

**Used On:** Airport and Heliport SID/STAR/Approach, Enroute Airway Records
**Length:** 4 characters
**Character Type:** Distance - Numeric; Time - Alpha/numeric
**Examples:** 1076, 2822, T010, 0208, 0016
</details>

<details>
<summary>5.28 - Inbound Magnetic Course (IB MAG CRS)</summary>

**Definition/Description:** "Inbound Magnetic Course" is the published inbound magnetic course to the waypoint in the "Fix Ident" field of the records in which it is employed.

The "HX" group of Path Terminator codes are used to provide racetrack type course reversal flight paths. Government publications for these course reversal include an "inbound magnetic bearing." The SID/STAR/Approach Procedures records do not include a dedicated field for this inbound course. Instead, the information is included in the "Outbound Magnetic Course" field of such records.

**Source/Content:** Values from official government sources will be used when available. The field contains magnetic bearing in degrees and tenths of a degree, with the decimal point suppressed. For routes charted with true courses, the last character of this field will contain a "T" in place of tenths of a degree.

**Used On:** Enroute Airways records
**Length:** 4 characters
**Character Type:** Alpha/numeric
**Examples:** 2760, 0231, 194T
</details>

<details>
<summary>5.29 - Altitude Description (ALT DESC)</summary>

**Definition/Description:** The "Altitude Description" field will designate whether a waypoint should be crossed "at," "at or above," "at or below" or "at or above to at or below" specified altitudes.

**Source/Content:** A code from the following table:

| Field Content | Waypoint Crossing Description |
|---|---|
| + (plus) | "At or above" altitude specified in first "Altitude" field. |
| - (minus) | "At or below" altitude specified in first "Altitude" field. |
| @ (blank) | "At" altitude specified in first "Altitude" field. |
| B | "At or above to at or below" altitudes specified in the first and second "Altitude" fields. |
| C | "At or above" altitude specified in second "Altitude" field. |
| G | Glide Slope altitude (MSL) at waypoint specified in second "Altitude" field (FAF), "at" altitude in first "Altitude" field. |
| H | Glide Slope altitude (MSL) at waypoint specified in second "Altitude" field (FAF), "at or above" altitude in first "Altitude" field, "at" altitude in second "Altitude" field. |
| I | Second "Altitude" field contains Glide Slope intercept altitude (FACF), "at" altitude in first "Altitude" field. |
| J | Second "Altitude" field contains Glide Slope intercept altitude (FACF), "at or above" altitude in first "Altitude" field. |
| V | "At or above" altitude for Stepdown Fix in Final Approach |

Note: The "B" entry may only appear in Airport and Heliport SID/STAR/Approach Route, Airport/Enroute/Heliport Communications, VHF Navaid Limitation and Preferred Route Records. The higher value will always appear first in records with two altitude fields, or as the first three digits of the Altitude Limitation field. In Approach Records, use is limited to Approach Transitions with the exception of the last leg of a transition and to Missed Approach with the exception of the first leg of a missed approach.

Note: The "C" entry may only appear in SID records. It is used to indicate that the leg has a conditional altitude termination.

Note: In Final Approach Route Coding, the codes "@ (for blank)," "G," "H," "I," "J," and "V" are applied as indicated in the table above. For more detail refer to procedure coding rules in Attachment 5 of this Specification.

**Used On:** Airport and Heliport SID/STAR/Approach, Airport, Heliport and Enroute Communications, VHF NAVAID Limitation Continuation, Preferred Routes and Flight Planning Arrival/Departure Data Records.
**Length:** One character
**Character Type:** Alpha or blank
</details>

<details>
<summary>5.30 - Altitude/Minimum Altitude</summary>

**Definition/Description:** The "Altitude/Minimum Altitude" field indicates the reference altitude associated with (1) Enroute Airways (MEA, MFA or other minimum altitudes as defined by source), (2) holding pattern path of Holding Pattern record, (3) terminal procedure path termination defined by the Path Terminator in the Airport or Heliport SID/STAR/Approach Record and (4) lowest altitude of the "blocked altitudes" for a Preferred Route.

**Source/Content:** Reference altitudes are determined during route definition. The values are derived from official government source when available. The field may contain altitudes (all numeric) or flight level (alpha/numeric). The all-numeric fields will contain altitudes in feet with a resolution of one foot. The alpha/numeric fields will contain the alpha characters "FL" followed by the altitude expressed in hundreds of feet (three digits) or a code as indicated below.

On Airport and Heliport SID, STAR and Approach Route records, the first "Altitude" field will contain an altitude when "Altitude Description" field contains a plus (+), a minus (-), or a "B," "C," "G," "H," "I," "J," or "V". The first "Altitude" field may contain an altitude when the "Altitude Description" field contains a "blank." The second "Altitude" field will contain an altitude when Altitude Description field contains a "B," "C," "G," "H," "I," "J," or "V".

On Enroute Airway records, the first "Minimum Altitude" field will contain the MEA or MFA if the altitude is the same for both directions of flight and the second "Minimum Altitude" will be blank. If the airway segment has directional MEAs/MFAs, the first "Minimum Altitude" field will contain the value for the direction of flight in which the airway is coded and the second "Minimum Altitude" field will contain the value for the opposite direction of flight. The first "Minimum Altitude" field may contain the alpha characters UNKNN when the MEA/MFA is unknown or the alpha characters NESTB when the MEA/MFA has not been established by the appropriate authority.

On Preferred Routes, the "Minimum Altitude" and the "Maximum Altitude" apply to the entire route and are a minimum and maximum block. Altitude 1 and Altitude 2 are fix related, apply only to the fix in the sequence in which they occur and are defined by the Altitude Description field.

**Used On:** Airport and Heliport SID/STAR/Approach, Holding Pattern, Enroute Airway, Preferred Routes.
**Length:** 5 characters
**Character Type:** Alpha/numeric
**Examples:** 05000, 18000, 00600, FL290, (UNKNN or NESTB on Enroute Airways)
</details>

<details>
<summary>5.31 - File Record Number (FRN)</summary>

**Definition/Description:** The "File Record Number" is a reference number assigned to the record for housekeeping purposes. Records are numbered consecutively, the first record on the tape being assigned the number 00001, the second the number 00002, and so on through the final record on the tape. File record numbers are subject to change at each tape update.

**Source/Content:** File record numbers are assigned to records during the assembly of the data file. If the file reaches 99999, the next record number will start over with 00000.

**Used On:** All records
**Length:** 5 characters
**Character Type:** Numeric
**Examples:** 10640, 00420, 31462
</details>

<details>
<summary>5.32 - Cycle Date (CYCLE)</summary>

**Definition/Description:** The "Cycle Date" field identifies the calendar period in which the record was added to the file or last revised. A change in any ARINC 424 field, except Dynamic Magnetic Variation, Frequency Protection, Continuation Record Number and File Record Number, requires a cycle date change. The cycle date will not change if there is no change in the data.

**Source/Content:** The first two digits of the field contain the last two digits of the year in which the addition or revision was made. The last two digits contain the numeric identity of the 28-day data update cycle during which the change occurred. Each calendar year contains 13 such cycles, however, on rare occasions 14 cycles will be encountered.

**Used On:** All records
**Length:** 4 characters
**Character Type:** Numeric
</details>

<details>
<summary>5.33 - VOR/NDB Identifier (VOR IDENT/NDB IDENT)</summary>

**Definition/Description:** The "VOR/NDB Identifier" field identifies the VHF/MF/LF facility defined in the record.

**Source/Content:** The field contains the official government 1-, 2-, 3- and 4-character facility identification code.

**Used On:** VHF NAVAIDs, NDB NAVAIDs, Airport Localizer Marker records
**Length:** 4 characters max
**Character Type:** Alpha/numeric
**Examples:** DEN, 6YA, PPI, TIKX
</details>

<details>
<summary>5.34 - VOR/NDB Frequency (VOR/NDB FREQ)</summary>

**Definition/Description:** The "VOR/NDB Frequency" field specifies the frequency of the NAVAID identified in the "VOR/NDB Identifier" field of the record.

**Source/Content:** Frequencies are derived from official government sources. VHF NAVAID frequencies contain characters for hundreds, tens, units, tenths and hundredths of megahertz. NDB frequencies contain characters for thousands, hundreds, tens, units and tenths of kilohertz. The decimal point following the unit entry is suppressed in both cases.

**Used On:** VHF NAVAID, NDB NAVAID, Airport Localizer Marker records
**Length:** 5 characters
**Character Type:** Numeric
**Examples:** VHF 11630, 11795 / NDB 03620, 17040
</details>

<details>
<summary>5.35 - NAVAID Class (CLASS)</summary>

**Definition/Description:** The "Class" field identifies the class of the NAVAID facility.

**Source/Content:** See Table below.

Колонки 28-32 (VHF NAVAID, ILS, MLS):

| Code | Facility |
|---|---|
| V | VOR |
| T | TACAN (channels 17-59 & 70-126) |
| M | TACAN (channels 1-16 & 60-69) |
| D | DME |
| I | ILS/DME or ILS/TACAN |
| N | MLS DME/N |
| P | MLS DME/P |
| T | Terminal |
| L | Low Altitude |
| H | High Altitude |
| U | Unrestricted (See Note 3) |
| C | TACAN part of ILS (See Note 4) |
| D | Biased ILS/DME or ILS/TACAN |
| A | Automatic Trans Weather Brdcst |
| B | Scheduled Weather Brdcst |
| W | No Voice on NAVAID Freq (See Note 7) |
| N | Non-Colocated VOR and TACAN or DME (See Note 1) |

Колонки 75-79 (L/MF NAVAID):

| Code | Facility |
|---|---|
| H | NDB |
| S | SABH |
| M | Marine Beacon |
| I | Inner Marker |
| M | Middle Marker |
| O | Outer Marker |
| C | Backcourse Marker |
| H | 2000 watts or more |
| M | 25 to 50 watts |
| L | Less than 25 watts (See Note 6) |
| A | Automatic Trans Weather Brdcst |
| B | Scheduled Weather Brdcst |
| W | No Voice on NAVAID Freq (See Note 7) |
| B | BFO Operation Required (See Note 5) |
| A | Locator/Marker colocated (See Note 2) |
| N | Locator/Marker non-colocated (See Note 2) |

NOTES:

1. The character "N" is entered into column 32 on VHF NAVAID records if either the latitudes and/or longitudes of the VOR and TACAN or DME components of a frequency-paired VHF NAVAID differ by 1/10 arc minutes or more. The column is "blank" for VHF NAVAIDs that are colocated or where the differences in both latitudes and longitudes is less than 1/10 arc minutes. The Character "N" is also entered into column 32 on DME or TACAN records when these are frequency-paired with a Localizer and the latitudes and/or longitudes of the Localizer and TACAN or DME differ by 1/10 arc minutes or more.
2. The character "N" is entered into column 79 on Airport Localizer Marker Records (PM) when the Marker and an associated Locator latitudes and/or longitudes differ by 1/10 arc minutes or more. The character "A" is entered into column 79 on Airport Localizer Marker Records (PM) when for the Marker and an associated Locator, both latitudes and longitudes differ by less than 1/10 arc minutes and at least one is non-zero. Column 79 in this record type is "blank" when the Marker and associated Locator are colocated.
3. The character "U" is entered into column 30 on VHF NAVAID Records when the official government source has not restricted the use of the facility by range or altitude.
4. The character "C" is entered into column 30 on VHF NAVAID Records when that record contains a TACAN Facility that is frequency paired with a Localizer and has the same identifier. It is for civil-use TACAN channels only. When "C" is coded in column 30, the "T" value (Terminal) is understood to apply also.
5. The character "B" is entered into column 32 of an NDB NAVAID Record or column 79 of an Airport Localizer Marker Record when the emission of the NDB or Locator requires BFO (Beat Frequency Oscillator) operation.
6. Column 30 of a NDB NAVAID and column 77 of Airport Localizer Marker Record is "blank" when the output power of the NDB or Locator is between 50 and 1999 watts.
7. Column 31 of the VHF and NDB NAVAID or column 78 of the Airport Localizer Marker Record is "blank" when there is "Voice Transmission Capability" on the NAVAID frequency. This column will always be "blank" on VHF NAVAID Records for TACAN or DME.

**Used On:** NAVAID Records (VHF, NDB and Terminal NDB), Airport Localizer Marker Records
**Length:** 5 characters max
**Character Type:** Alpha
</details>

<details>
<summary>5.36 - Latitude (LATITUDE)</summary>

**Definition/Description:** The "Latitude" field contains the latitude of the navigational feature identified in the record.

**Source/Content:** Geographic positions whose latitudes must be included in the data base are defined during route design, many of them in official government publications. The field is constructed as follows. The first character position contains the alpha character "N" or "S" indicating whether the latitude is north or south of the equator. "N" is entered for latitudes falling on the equator. The following eight numeric characters define the latitude in degrees, minutes, seconds, tenths of seconds and hundredths of seconds. Degree, minute and second symbols and the decimal point are suppressed.

Note: Some RNAV system users may elect to round off latitude values to resolutions of less than one hundredth of a second prior to the entry of these data into the airborne computer.

The navigation reference points to be defined by latitude and longitude coordinates are listed in Figure 5-8.

**Figure 5-8** (Record File → Lat/Long Field Location Defined):

| Record File | Location Defined |
|---|---|
| Airport | Aerodrome Reference Point |
| Airport Comm (See Note 7) | Comm Transmitter Antenna |
| Enroute Comm (See Note 7) | Comm Transmitter Antenna |
| Enroute Marker | Marker Antenna |
| FIR/UIR | FIR/UIR Boundary Position |
| FIR/UIR Arc Origin | Center of Arc |
| Gate | Gate |
| Heliport | Helipad |
| Heliport Comm | Comm Transmitter Antenna |
| Localizer | Localizer Antenna |
| Localizer Glide Slope (See Note 6) | Glide Slope Antenna |
| Marker/Locator | Marker Beacon Antenna / Locator Antenna |
| NDB Navaid | NDB Antenna |
| Restr. Airspace | Restr. Airspace Boundary Position |
| Restr. Airspace Arc Origin | Center of Arc |
| VHF Navaid VOR (See Note 1) | VOR Antenna |
| VHF Navaid DME or TACAN (See Note 2) | DME or TACAN Antenna |
| Runway (See Note 5) | Runway Landing Threshold |
| Waypoint | Waypoint |
| MLS Azimuth | Azimuth Antenna |
| MLS Elevation | Elevation Antenna |
| MLS Back Azimuth (See Note 3) | Back Azimuth Antenna |
| MLS Datum (See Note 4) | MLS Reference Datum Point |

Note 1: The VOR latitude and longitude fields are filled when the "NAVAID Class" field contains the letter "V" in column 28 of the record. If column 28 is blank, these fields are blank also.

Note 2: The DME or TACAN latitude and longitude fields are filled when the "NAVAID Class" field contains the letters "D," "I" "M," "N," "P" or "T" in column 29 of the record. If column 29 is blank, these fields are blank also.

Note 3: The MLS Back Azimuth latitude and longitude fields are to be left blank where no such facility exists.

Note 4: MLS Datum is the point on the runway center line closest to the phase center of the approach elevation antenna.

Note 5: The Runway latitude and longitude fields define the Runway Landing Threshold. This threshold can be the beginning of the landing runway pavement. It will be the displaced threshold (inward from the beginning of the landing runway pavement) when such is published by official government documentation.

Note 6: Localizer Glide Slope latitude and longitude may be blank when detail not available through source documentation.

Note 7: On Communications Records, the Latitude and Longitude always define the transmitter antenna site, regardless if that site is a Remote Communications Outlet or independent transmitter position not associated with a Navaid.

**Used On:** NAVAID, Waypoint, Airport and Heliport ILS, Airport, Gate, Runway, Airport and Heliport Localizer Marker, Airport and Heliport MLS and GLS, Airport and Heliport MLS Continuation, Airway Marker, Airport and Heliport Communications, Enroute Communications, Heliport, Restrictive Airspace, FIR/UIR, Controlled Airspace, Path Point and GLS Records.
**Length:** 9 characters
**Character Type:** Alpha/numeric
**Examples:** N39513881
</details>

<details>
<summary>5.37 - Longitude (LONGITUDE)</summary>

**Definition/Description:** The Longitude field contains the longitude of the geographic position of the navigational feature identified in the record.

**Source/Content:** Geographic positions whose longitudes must be included in the data base are defined during route design, many of them in official government publications. The field is constructed as follows: The first character position will contain the alpha character "E" or "W," indicating whether the longitude is east or west of the prime (zero degree) meridian. For longitudes falling on the 0 or 180 degree meridians, "E" is entered. The following nine numeric characters define the longitude in degrees, minutes, seconds, tenths of seconds and hundredths of seconds. Degree, minute and second symbols and the decimal point are suppressed.

Note: Some RNAV system users may elect to round off longitude values to resolutions of less than one hundredth of a second prior to the entry of these data into the airborne computer.

The navigation reference points to be defined by latitude and longitude coordinates are listed in Figure 5-8.

**Used On:** NAVAID, Waypoint, Airport and Heliport ILS, Airport, Gate, Runway, Airport and Heliport Localizer Marker, Airport and Heliport MLS, GLS Airports and Heliport MLS Continuation, Airway Marker, Airport and Heliport Communications, Enroute Communications, Heliport, Restrictive Airspace, FIR/UIR, Controlled Airspace, Path Point and GLS Records.
**Length:** 10 characters
**Character Type:** Alpha/numeric
**Examples:** W104450794
</details>

<details>
<summary>5.38 - DME Identifier (DME IDENT)</summary>

**Definition/Description:** The identification of a DME facility, a TACAN facility or the DME (or TACAN) component of a VORDME or VORTAC facility.

**Source/Content:** The "DME Identifier" field will contain the officially published 2-, 3-, or 4-character DME facility identifier. For VOR/DME and VORTAC facilities, if the identification codes of the VOR and DME components of the NAVAID defined in the record are the same, the field will be blank. If they are not the same, the VOR Identification will be as defined in Section 5.33 and the DME Identifier field will carry the identification of the DME component. The field is blank when the VHF Navaid facility in the reference record has no DME component. The field will always contain the DME Identifier for TACANs, DME Only NAVAIDS and Localizer or MLS DME facilities.

**Used On:** VHF NAVAID records
**Length:** 4 characters max
**Character Type:** Alpha/numeric
**Examples:** MCR, DEN, IDVR, DN, (Blank)
</details>

<details>
<summary>5.39 - Magnetic Variation (MAG VAR, D MAG VAR)</summary>

**Definition/Description:** The "Magnetic Variation" field specifies the angular difference between True North and Magnetic North at the location defined in the record. "Dynamic Magnetic Variation" is a computer model derived value and takes location and date into consideration. For the "Station Declination" used in some record types, refer to Section 5.66.

**Source/Content:** Magnetic variations are obtained from official government data sources and other geographical magnetic variation source. A number of different terms are used in government documentation that have specific connotations for the information provided by that government. The most common is "Epoch Year Variation." In theory, this is a value determined by a government agency once every five years and published for general use. Along with Epoch Year Variation, some governments also publish an annual drift value. Data suppliers do not include annual drift derived figures in their databases but rather stay with the Epoch Year value. Another term encountered in source documentation is "Magnetic Variation of Record." This is generally an Epoch Year value. The difference here is that the government authority has established the value as valid for everything associated with a given location. For example, if a Magnetic Variation of Record is established for an airport location, everything referenced to that airport will use the same value. This is of interest as it means that Terminal Procedure design is also based on that value. Obvious differences can occur between a database supplied, semi-static value, and a value derived dynamically, either by the airborne systems or supplier ground systems. Dynamic Magnetic Variation, contained in the VHF Navaid Continuation Record and Enroute/Terminal Waypoint Primary Records, is a computed, earth model derived figure, and is updated dynamically on a schedule established by the data base supplier. Position one of the field contains an alpha character taken from the table below followed by the value of magnetic variation expressed in degrees and tenths of a degree, with the decimal point suppressed. When the first column is coded with the character "T," the value will be all zeros.

| Field Entry | Description |
|---|---|
| E | Magnetic variation is East of TRUE North |
| W | Magnetic variation is West of TRUE North |
| T | The element defined in the current record is oriented to TRUE North in an area in which the local variation is not zero. |

**Used On:** Airport, NDB Navaid, Airport Localizer Marker, MLS, GLS, Airway Marker, Enroute/Airport/Heliport Communication, Heliport, Enroute Waypoint, Airport and Heliport Terminal Waypoint and GLS Primary Records and VHF Navaid Continuation Records.
**Length:** 5 characters
**Character Type:** Alpha/numeric
**Examples:** E0140, E0000, T0000
</details>

<details>
<summary>5.40 - DME Elevation (DME ELEV)</summary>

**Definition/Description:** The "DME Elevation" field defines the elevation of the DME component of the NAVAID described in the record.

**Source/Content:** DME elevations specified in official government publications are entered into this field in feet with respect to MSL. When the elevation is below MSL, the first column of the field contains a minus (-) sign.

**Used On:** VHF NAVAID records
**Length:** 5 characters
**Character Type:** Alpha/numeric
**Examples:** 00530, -0140
</details>

<details>
<summary>5.41 - Region Code (REGN CODE)</summary>

**Definition/Description:** The "Region Code" permits the categorization of waypoints and holding patterns as either enroute or terminal area waypoints. In the latter case the terminal area airport is identified in the field.

**Source/Content:** The field contains the alpha characters ENRT for enroute waypoints and airport identification code (Airport Ident) for terminal waypoints. In the holding pattern file, the content will match that of the holding fix, e.g. if the holding fix is an enroute waypoint or enroute Navaid, the content will be ENRT; if the holding fix is a terminal waypoint or terminal NDB, the content will be the airport identification.

**Used On:** Waypoint and Holding Pattern records
**Length:** 4 characters
**Character Type:** Alpha/numeric
**Examples:** ENRT, KLAX, 9V9
</details>

<details>
<summary>5.42 - Waypoint Type (TYPE)</summary>

**Definition/Description:** The "Waypoint Type" field defines both a "type" for a waypoint and a "function" for a waypoint within the waypoint file.

**Source Content:** The following tables define available "Waypoint Type" codes:

ENROUTE WAYPOINT:

| Waypoint Type | Col 27 | Col 28 | Col 29 |
|---|---|---|---|
| Combined Named Intersection and RNAV | C | | |
| Unnamed, Charted Intersection | I | Note 1 | Note 2 |
| NDB Navaid as Waypoint | N | | |
| Named Intersection | R | | |
| Uncharted Airway Intersection | U | | |
| RNAV Waypoint | W | | |

ENROUTE AND TERMINAL WAYPOINT (коды Col 29):

| Waypoint Type | Col 29 |
|---|---|
| SID | D |
| STAR | E |
| Approach | F |
| Multiple | Z |
| Final Approach Fix | A |
| Initial and Final Approach Fix | B |
| Final Approach Course Fix | C |
| Intermediate Approach Fix | D |
| Off-Route Intersection | F |
| Initial Approach Fix | I |
| Final Approach Course Fix at Initial Approach Fix | K |
| Final Approach Course Fix at Intermediate Approach Fix | L |
| Missed Approach Fix | M |
| Initial Approach Fix and Missed Approach Fix | N |
| Oceanic Entry/Exit Waypoint | O |
| FIR/UIR or Controlled Airspace Intersection | U |
| Latitude/Longitude Intersection, Full Degree of Latitude | V |
| Latitude/Longitude Intersection, Half Degree of Latitude | W |

TERMINAL WAYPOINT:

| Waypoint Type | Col 27 | Col 28 | Col 29 |
|---|---|---|---|
| ARC Center Fix Waypoint | A | Note 3 | Note 3 |
| Combined Named Intersection and RNAV Waypoint | C | | |
| Unnamed, Charted Intersection | I | Note 1 | Note 2 |
| Middle Marker as Waypoint | M | | |
| Terminal NDB Navaid as Waypoint | N | | |
| Outer Marker as Waypoint | O | | |
| Named Intersection | R | | |
| RNAV Waypoint | W | | |
| Final Approach Fix | | | A |
| Initial Approach Fix and Final Approach Fix | | | B |
| Final Approach Course Fix | | | C |
| Intermediate Approach Fix | | | D |
| Initial Approach Fix | | | I |
| Final Approach Course Fix at Initial Approach Fix | | | K |
| Final Approach Course Fix at Intermediate Approach Fix | | | L |
| Missed Approach Fix | | | M |
| Initial Approach Fix and Missed Approach Fix | | | N |
| Unnamed Stepdown Fix | | | P |
| Named Stepdown Fix | | | S |
| FIR/UIR or Controlled Airspace Intersection | | | U |

Note 1: Column 28 of the Enroute and Terminal Waypoint Types will always be blank when column 27 carries the "N" for NDB or Terminal NDB produced as Waypoints.

Note 2: Possible codes for column 29 are identical for both Enroute and Terminal Waypoints and are those carried in the third portion of the table. Column 29 will always be blank when column 27 carries the "N" for NDB or Terminal NDB produced as Waypoints.

Note 3: When column 27 equals "A" for ARC Center Fix Waypoint, columns 28 and 29 will always be blank.

**Used On:** Enroute Waypoints, Airport and Heliport Terminal Waypoints.
**Length:** 3 characters
**Character Type:** Alpha
</details>

<details>
<summary>5.43 - Waypoint Name/Description (NAME/DESC)</summary>

**Definition/Description:** The "Waypoint Name/Description" field sets the unabbreviated name of a named waypoint or a definition of an unnamed waypoint.

**Source/Content:** The name of a named waypoint is spelled out in full. Definitions for unnamed waypoints are described in Chapter 7 of this specification.

**Used On:** Enroute Waypoints, Airport and Heliport Terminal Waypoints.
**Length:** 25 characters max
**Character Type:** Alpha/numeric
**Examples:** FORT SMITH, LAX04026, LOS235/110, 6100N01234W (OCTA), OM RW26L ALTUR
</details>

<details>
<summary>5.44 - Localizer/MLS/GLS Identifier (LOC, MLS, GLS IDENT)</summary>

**Definition/Description:** The "Localizer/MLS/GLS Identifier" field identifies the localizer, MLS facility or GLS Ref Path defined in the record. In the Runway Record, two "Landing Systems" may be defined.

**Source/Content:** The field contains the identification code of the Localizer or MLS facility or GLS Reference Path derived from official government sources. In the Runway Record, there are two fields labeled Localizer/MLS/GLS Reference Path identifier and second Localizer/MLS/GLS Reference Path identifier to encode multiple Localizers, such as an ILS and a LDA associated with a single runway.

**Used On:** Runway, Localizer, Localizer Marker, MLS, MLS Continuation and GLS Record.
**Length:** 4 Characters max
**Character Type:** Alpha/Numeric
**Examples:** Localizer - IDEN, ISTX, IDU, PP; MLS - MDEN, MSTX, MLAX; GLS - LFBL, EGLC, KSAN
</details>

<details>
<summary>5.45 - Localizer Frequency (FREQ)</summary>

**Definition/Description:** The "Localizer Frequency" field specifies the VHF frequency of the facility identified in the "Localizer Identifier" field.

**Source/Content:** The official government-source localizer frequency is entered into the field with a resolution of 50 kHz. The decimal point following the unit MHz entry is suppressed.

**Used On:** Airport and Heliport ILS Localizer records
**Length:** 5 characters
**Character Type:** Numeric
**Examples:** 11030, 11195
</details>

<details>
<summary>5.46 - Runway Identifier (RUNWAY ID)</summary>

**Definition/Description:** The "Runway Identifier" field identifies the runways described in runway records and runways served by the ILS/MLS described in ILS/MLS records.

**Source/Content:** Runway identifiers are derived from official government sources and are shown in the following format: The two letters "RW" are followed by two numerics, 01 thru 36, and may contain a fifth character designation of one of the following:

| Code | Описание |
|---|---|
| C | Center (Runway of three parallel runways) |
| L | Left (Runway of two or three parallel runways) |
| R | Right (Runway of two or three parallel runways) |
| T | (Runway and associated flight maneuvers referenced only in degrees true) |

Any other designations (suffixes), such as North, South, East, West or STOL will not be included in the ARINC file.

**Used On:** Airport and Heliport ILS and MLS, GLS Runway, Airport and Heliport Localizer Marker, Path Point and GLS Records.
**Length:** 5 characters max
**Character Type:** Alpha/numeric
**Examples:** RW26L, RW08R, RW26C, RW05, RW17T
</details>

<details>
<summary>5.47 - Localizer Bearing (LOC BRG)</summary>

**Definition/Description:** The "Localizer Bearing" field defines the magnetic bearing of the localizer course of the ILS facility/GLS approach described in the record.

**Source/Content:** Localizer courses, derived from official government sources, are entered into the field in degrees and tenths of a degree, with the decimal point suppressed. For localizer courses charted with true courses, the last character of this field will contain a "T" in place of tenths of a degree.

**Used On:** ILS, GLS records
**Length:** 4 characters
**Character Type:** Alpha/Numeric
**Examples:** 2570, 0147, 2910, 347T
</details>

<details>
<summary>5.48 - Localizer Position (LOC FR RW END) Azimuth/Back Azimuth Position (AZ/BAZ FR RW END)</summary>

**Definition/Description:** The "Localizer/Azimuth Position" field defines the location of the facility antenna relative to one end of the runway.

**Source/Content:** The field contains the official government source distance, in feet, from the antenna to the runway end. The resolution is one foot.

**Used On:** ILS, MLS and MLS Continuation records
**Length:** 4 characters
**Character Type:** Numeric
**Examples:** 0950, 1000
</details>

<details>
<summary>5.49 - Localizer/Azimuth Position Reference (@,+,-)</summary>

**Definition/Description:** The "Localizer/Azimuth Position Reference" field indicates whether the antenna is situated beyond the stop end of the runway, ahead of or beyond the approach end of the runway. The "Back Azimuth Position Reference" field indicates whether the antenna is situated ahead of the approach end of the runway, ahead of or beyond the stop end of the runway.

**Source/Content:** For Localizer and Azimuth positions the field is blank (@) when the antenna is situated beyond the stop end of the runway, it contains a plus (+) sign when the antenna is situated ahead of the approach end of the runway or a minus (-) sign when it is located off to one side of the runway. For Back Azimuth positions the field is blank (@) when the antenna is situated ahead of the approach end of the runway, it contains a plus (+) sign when the antenna is situated beyond the stop end of the runway or a minus (-) sign when it is located off to one side of the runway.

**Used On:** ILS, MLS and MLS Continuation records
**Length:** One character
**Character Type:** Alpha
</details>

<details>
<summary>5.50 - Glide Slope Position (GS FR RW THRES) Elevation Position (EL FR RW THRES)</summary>

**Definition/Description:** The "Glide Slope/Elevation Position" field defines the location of the antenna with respect to the approach end of the runway.

**Source/Content:** The field contains four numeric characters indicating the distance in feet (to a resolution of one foot) from a line drawn at right angles to the runway at the antenna position to the threshold of the runway.

**Used On:** ILS and MLS records
**Length:** 4 characters max
**Character Type:** Numeric
**Examples:** 0980, 1417
</details>

<details>
<summary>5.51 - Localizer Width (LOC WIDTH)</summary>

**Definition/Description:** The "Localizer Width" field specifies the localizer course width of the ILS facility defined in the record.

**Source/Content:** Localizer course widths from official government sources are entered into the field in degrees, tenths of a degree and hundredths of a degree with the decimal point suppressed.

**Used On:** ILS records
**Length:** 4 characters
**Character Type:** Numeric
**Examples:** 0500, 0400, 0350
</details>

<details>
<summary>5.52 - Glide Slope Angle (GS ANGLE) Minimum Elevation Angle (MIN ELEV ANGLE)</summary>

**Definition/Description:** The "Glide Slope Angle" field defines the glide slope angle of an ILS facility/GLS approach. The "Minimum Elevation Angle" field defines the lowest elevation angle authorized for the MLS procedure.

**Source/Content:** Glide Slope and Elevation angles from official government sources are entered into the fields in degrees, tenths of a degree and hundredths of a degree with the decimal point suppressed.

**Used On:** ILS, GLS and MLS records
**Length:** 3 Characters
**Character Type:** Numeric
**Example:** 275, 300
</details>

<details>
<summary>5.53 - Transition Altitude/Level (TRANS ALTITUDE/LEVEL)</summary>

**Definition/Description:** The "Transition Altitude" field defines the altitude in the vicinity of an airport or heliport at or below which the vertical position of an aircraft is controlled by reference to altitudes (MSL). The "Transition Level" field defines the lowest flight level available for use above the transition altitude. Aircraft descending through the transition layer will use altimeters set to local station pressure, while departing aircraft climbing through the layer will be using standard altimeter setting (QNE) of 29.92 inches of mercury, 1013.2 millibars or 1013.2 hectopascals.

**Source/Content:** Transition Altitudes/Levels are derived from official government sources. For STAR and Approach records, the field defines the level, expressed in feet, at which the altimeter barometric setting is changed from standard to local values for the airport or heliport identified in the record. For SID records, the field will contain the Transition Altitude expressed in feet. The first leg of each Airport and Heliport SID/STAR/Approach procedure shall contain the appropriate transition altitude with a resolution of one foot. If the transition altitude is unknown or "by ATC," the field will be blank in procedure records. For Airport and Heliport records, the Transition Altitude and Transition Level will be entered into the appropriate fields, in feet with a resolution of one foot. If the Transition Altitude or Level is unknown, "by ATC" or has different values for varying procedures at the airport or heliport, the field will be blank.

**Used On:** Airport and Heliport SID/STAR/Approach, Airport and Heliport Records
**Length:** 5 characters
**Character Type:** Numeric
**Examples:** 05000, 23000, 18000
</details>

<details>
<summary>5.54 - Longest Runway (LONGEST RWY)</summary>

**Definition/Description:** The "Longest Runway" field permits airport to be classified on the basis of the longest operational hard-surface runway.

**Source/Content:** The longest runway will be derived from official government sources and entered in the field in hundreds of feet. This value will represent the longest hard-surfaced operational runway available without restriction at the airport. The value reflects overall pavement length declared suitable and available for the ground operations of aircraft. Where no hard-surfaced runway is available or those available do not meet criteria, the value will represent the longest operational runway at the airport.

**Used On:** Airport Records
**Length:** 3 characters
**Character Type:** Numeric
**Examples:** 040, 055, 098, 111
</details>

<details>
<summary>5.55 - Airport/Heliport Elevation (ELEV)</summary>

**Definition/Description:** The elevation of the airport/Heliport specified in the record is defined in the "Airport Elevation" and "Heliport Elevation" field.

**Source/Content:** Airport/Heliport elevations are to be derived from official government sources and entered into the field in feet to a resolution of one foot. For elevations above MSL, the field contains the numeric characters of the elevation only. For below MSL elevations the first character of the field is a minus (-) sign. In most cases, airport elevation is defined as the highest elevation of any landing surface on the airport.

**Used On:** Airport and Heliport records
**Length:** 5 characters
**Character Type:** Alpha/numeric
**Examples:** 02171, -0142, 05230
</details>

<details>
<summary>5.60 - Notes (Primary Records) (NOTES)</summary>

**Definition/Description:** The "Notes" field provides space in the record for information supplementary to that contained in the encoded part of the record.

**Source/Content:** Appropriate contents for the field will be determined when the record is assembled.

**Used On:** Gate and Holding Pattern records
**Length:** 22 characters max
**Character Type:** Alpha/numeric
**Examples:** HOLDING JIMEE MIAMI
</details>

<details>
<summary>5.61 - Notes (Continuation Records) (NOTES)</summary>

**Definition/Description:** The "Notes" field (continuation record) is provided to accommodate any information that cannot be entered in the primary record.

**Source/Content:** Appropriate contents for the field will be determined at the time the primary record is assembled.

**Used On:** All except Company route records
**Length:** 70 characters max
**Character Type:** Alpha/numeric
**Examples:** EASTBOUND PREFERRED 090/0Z/230/0Z
</details>

<details>
<summary>5.62 - Inbound Holding Course (IB HOLD CRS)</summary>

**Definition/Description:** The "Inbound Holding Course" field defines the inbound course to the holding waypoint.

**Source/Content:** Inbound holding courses derived from official government sources are entered into the field in degrees and tenths of a degree, with the decimal point suppressed. For holding courses charted with true bearings, the last character of this field contains a "T" in place of tenths of a degree.

**Used On:** Holding Pattern records
**Length:** 4 characters
**Character Type:** Alpha/numeric
**Examples:** 0456, 1800, 3034, 347T
</details>

<details>
<summary>5.63 - Turn (TURN)</summary>

**Definition/Description:** The "Turn" field specifies the direction in which holding pattern turns are to be made.

**Source/Content:** The "Turn" field will always contain either L or R.

**Used On:** Holding Pattern records
**Length:** One character
**Character Type:** Alpha
</details>

<details>
<summary>5.64 - Leg Length (LEG LENGTH)</summary>

**Definition/Description:** The "Leg Length" field specifies the distance between the point at which the aircraft rolls out on the inbound leg of the holding pattern and the fix at which the holding pattern is defined (see Figure 5-10).

**Source/Content:** Leg length derived from official government sources is entered into the field in nautical miles and tenths of a nautical mile, with the decimal point suppressed.

**Used On:** Holding Pattern records
**Length:** 3 characters
**Character Type:** Numeric
**Examples:** 108, 055
</details>

<details>
<summary>5.65 - Leg Time (LEG TIME)</summary>

**Definition/Description:** The "Leg Time" field specifies the length of the inbound leg of a holding pattern in units of time (see Figure 5-10).

**Source/Content:** Leg time, derived from official government sources, is entered into this field in minutes and tenths of a minute, with the decimal point suppressed.

**Used On:** Holding Pattern records
**Length:** 2 characters
**Character Type:** Numeric
**Examples:** 10, 15, 20
</details>

<details>
<summary>5.66 - Station Declination (STN DEC)</summary>

**Definition/Description:** For VHF NAVAIDS, the "Station Declination" field contains the angular difference between true north and the zero degree radial of the NAVAID at the time the NAVAID was last site checked. For ILS localizers, the field contains the angular difference between true north and magnetic north at the localizer antenna site at the time the magnetic bearing of the localizer course was established.

**Source/Content:** Station declinations are derived from official government sources. The field contains one of the alpha characters shown in the following table followed by the value of the declination in degrees and tenths of a degree, with the decimal point suppressed. When the first column of the Station Declination field is coded T or G, the remainder of the field should be coded all zeros.

| Column 1 Character | Declination Description |
|---|---|
| E | Declination is East of True North |
| W | Declination is West of True North |
| T | Station is oriented to True North in an area in which the local variation is not zero. |
| G | Station is oriented to Grid North |

COMMENTARY: The appearance of the character "G" in column 1 of this field will alert users that although a NAVAID declination may not be zero, the fact that the grid reference is unknown prevents a value from being defined.

**Used On:** VHF NAVAID and ILS records
**Length:** 5 characters
**Character Type:** Alpha/Numeric
**Examples:** E0072, E0000, T0000, G0000
</details>

<details>
<summary>5.67 - Threshold Crossing Height (TCH)</summary>

**Definition/Description:** The "Threshold Crossing Height" specifies the height above the landing threshold on a normal glide path.

**Source/Content:** The Threshold Crossing Height will be derived from official government sources when available. For runway records the Glide Slope Height at landing threshold will be used for runways with ILS approaches. If an ILS is not available, it will be the RNAV waypoint height, if neither of these values is available it will be 50 feet.

**Used On:** Airport and Heliport ILS and MLS, Runway, and Path Point Records
**Length:** 2 characters
**Character Type:** Numeric
**Example:** 50
</details>

<details>
<summary>5.68 - Landing Threshold Elevation (LANDING THRES ELEV)</summary>

**Definition/Description:** The elevation of the landing threshold of the runway described in a runway record is defined in the "Landing Threshold Elevation" field.

**Source/Content:** Runway landing threshold elevations derived from official government sources are entered into this field in feet, to a resolution of 1 foot. For elevations above MSL, the field contains the numeric characters of the elevation only. For below MSL elevations, the first character of the field is a minus (-) sign.

**Used On:** Runway records
**Length:** 5 characters
**Character Type:** Alpha/numeric
**Examples:** 01250, -0150
</details>

<details>
<summary>5.69 - Threshold Displacement Distance (DSPLCD THR)</summary>

**Definition/Description:** The distance from the extremity of a runway to a threshold not located at that extremity of that runway.

**Source/Content:** Threshold displacement distances derived from official government sources are entered into this field in feet.

**Used On:** Runway records
**Length:** 4 characters
**Character Type:** Numeric
**Examples:** 0485, 1260
</details>

<details>
<summary>5.70 - Vertical Angle (VERT ANGLE)</summary>

**Definition/Description:** The "Vertical Angle" field defines the vertical navigation path prescribed for the procedure. The vertical angle should cause the aircraft to fly at the last coded altitude and descend on the angle, projected back from the fix and altitude at which the angle is coded. Vertical Angle information is provided only for descending vertical navigation. The angle is preceded by a "–" (minus sign) to indicate the descending flight.

**Source/Content:** Values from official government sources will be used when available. The angles are expressed in degrees, tenths, and hundredths of a degree, with the decimal point suppressed. Vertical Angle may also be coded as a calculated value as indicated in Attachment 5.

**Used On:** Airport and Heliport SID/STAR/Approach Records
**Length:** 4 characters
**Character Type:** Alpha/Numeric
**Examples:** -300, -375
</details>

<details>
<summary>5.71 - Name Field</summary>

**Definition/Description:** This field will be used to further define the record by name.

**Source/Content:** Facility name will be derived from official government sources. A parenthetical name following the official name may be used to identify the location of the facility.

**Used On:** Navaid, Airport, Heliport and Enroute Marker records
**Length:** 30 characters
**Character Type:** Alpha
</details>

<details>
<summary>5.72 - Speed Limit (SPEED LIMIT)</summary>

**Definition/Description:** The speed limit will be a maximum speed, expressed in K.I.A.S.

**Source/Content:** The speed limit will be derived from official government source documentation and shown in Knots on an applicable Airport or Heliport SID/STAR/Approach Record. On SIDs, the speed limit will apply to all legs up to and including the terminator of the leg on which the limit is encoded from the beginning of the procedure. If a second speed limit is coded on a subsequent leg, the limit will be applied from that leg backwards to the previous terminator which contained a speed limit. On STARs, the speed limit will be applied forward to the end of the arrival, (i.e. throughout the procedure until the end of the Flight Plan) unless a second speed limit is encoded. The intent in both SIDs and STARs is to exclude speed changes inconsistent with the procedure type. When used on Airport and Heliport records, the speed limit applies to all flight segments departing or arriving that Airport's or Heliport's terminal area, at and below the specified Speed Limit Altitude (see Section 5.73).

**Used On:** Airport and Heliport SID/STAR/Approach, Airport and Heliport, Flight Planning Arr/Dep Data Records
**Length:** 3 characters
**Character Type:** Numeric
**Examples:** 250
</details>

<details>
<summary>5.73 - Speed Limit Altitude</summary>

**Definition/Description:** "Speed Limit Altitude" is the altitude below which speed limits may be imposed.

**Source/Content:** The "Speed Limit Altitude" will be derived from official government sources in feet MSL or FL's.

**Used On:** Airport and Heliport records
**Length:** 5 characters
**Character Type:** Alpha/numeric
**Examples:** 10000, F125
</details>

<details>
<summary>5.74 - Component Elevation (GS ELEV, EL ELEV, AZ ELEV, BAZ ELEV)</summary>

**Definition/Description:** The "Component Elevation" field defines the elevation of a given component in the Localizer, GLS and MLS records. The "Glide Slope Elevation (GS ELEV)" defines the elevation of the Glide Slope component in the Localizer Records. The "EL Elevation (EL ELEV)" defines the elevation of the Elevation component of the MLS Record, the "Azimuth Elevation (AZ ELEV)" defines the elevation of the Azimuth component of the MLS Record and the "Back Azimuth Elevation (BAZ ELEV)" defines the elevation of the Back Azimuth component of the MLS Record. The "GLS station elevation (GLS ELEV)" defines the elevation of the GLS ground station in the GLS record.

**Source/Content:** Elevations specified in official government publications are entered in this field with respect to MSL. When the elevation is below MSL, the first column of the field contains a minus (-) sign.

**Used On:** Localizer, MLS and GLS Records and MLS Continuation Records
**Length:** 5 characters
**Character Type:** Alpha/numeric
**Examples:** 00235, 01265, -0011
</details>

<details>
<summary>5.75 - From/To - Airport/Fix</summary>

**Definition/Description:** When used on Company Routes, the "From Airport/Fix" is the waypoint from which the company route originates. The "To Airport/Fix" is the waypoint at which the company route terminates. When used on Alternate Records, it is the Departure, Destination or Enroute Airport/Fix for which the alternate information is being provided.

**Source/Content:** The customer is responsible for defining points at which company routes originate and terminate and for defining which departure, destination or enroute points are to have alternate information.

**Used On:** Company Route and Alternate Records
**Length:** 5 characters max.
**Character Type:** Alpha/numeric
</details>

<details>
<summary>5.76 - Company Route Ident SID/STAR/Awy (S/S/AWY)</summary>

**Definition/Description:** The "Company Route Ident" field identifies each unique route between origination and destination.

**Source/Content:** This field is determined by the customer.

**Used On:** Company Route records
**Length:** 10 characters
**Character Type:** Alpha/Numeric
</details>

<details>
<summary>5.77 - VIA Code</summary>

**Definition/Description:** The "VIA Code" field is used to define the type of route used in the SID/STAR/Approach/Airways field (Section 5.78) on Company Route records and defines the type of route used in the AWY Identifier on Preferred Route records. On the Preferred Route records, some codes define the use, or restriction to use, of a fix or routing.

**Source/Content:** The code to be entered shall be selected from the table below:

Company Route Record (R):

| VIA Field Content | Description |
|---|---|
| ALT | Alternate Airport |
| APP | Approach Route |
| AWY | Designated Airway |
| DIR | Direct to Fix |
| INT | Initial Fix |
| PRE | Preferred Route |
| SID | Standard Instrument Departure |
| SDE | Standard Instrument Departure - Enroute Transition |
| SDY | Standard Instrument Departure - Runway Transition |
| STR | Standard Terminal Arrival and Profile Descent |
| STE | Standard Terminal Arrival and Profile Descent - Enroute Transition |
| STY | Standard Terminal Arrival and Profile Descent - Runway Transition |

Preferred Route Record (ET):

| VIA Field Content | Description |
|---|---|
| AWY | Designated Airway |
| DIR | Direct to Fix |
| INT | Initial Fix |
| RVF | Route via Fix |
| RNF | Route via Fix not permitted |
| SID | Standard Instrument Departure |
| STR | Standard Terminal Arrival and Profile Descent |

**Used On:** Company Route and Preferred Route records
**Length:** 3 characters
**Character Type:** Alpha/numeric
**NOTE:** Figure 5-14 illustrates how various fields are to be completed in the Company Route Record based on the various "VIA Codes" defined in this paragraph.
</details>

<details>
<summary>5.78 - SID/STAR/App/AWY (S/S/A/AWY)</summary>

**Definition/Description:** This field is used to identify the particular route to be flown as referenced by the "VIA" field (5.77).

**Source/Content:** For Company Route records this field can contain the SID/STAR, Approach, Enroute Airway, or Preferred Route Identifier (see paragraphs, 5.8, 5.9, and 5.10). For Preferred Route records this field can contain the SID/STAR or Enroute Airway Route Identifier (see paragraph 5.8). This field will be blank for certain records depending on the "VIA" field content (5.77).

**Used On:** Company Route and Preferred Route Records
**Length:** 6 characters
**Character Type:** Alpha/numeric
**Examples:** VIA S/S/A/AWY: SIDCUIT8, STRLOCKE9, APPI19L, AWYJ501
</details>

<details>
<summary>5.79 - Stopway</summary>

**Definition/Description:** "Stopway" means the length of an area beyond the take-off runway, no less wide than the runway and centered upon the extended centerline of the runway, and designated for use in decelerating the airplane during an aborted takeoff.

**Source/Content:** The Stopway will be derived from official government sources and shown in feet. (See Figure 5-3).

**Used On:** Runway records
**Length:** 4 characters
**Character Type:** Numeric
**Examples:** 0900, 1000
</details>

<details>
<summary>5.80 - ILS Category (CAT)</summary>

**Definition/Description:** The Localizer/MLS/GLS Performance Categories have established operating minimums and are listed as Category I, II, and III. The level of Performance Category does not imply that permission exists to use the facility for landing guidance to that level and does not limit minima using designated classification. This field is also used to define the classification, non-ILS/MLS/GLS, and localizer installation such as IGS, LDA, or SDF. As used in the runway record, there are two fields, one labeled Localizer/MLS/GLS Category/Classification and the other labeled Second Localizer/MLS/GLS Category/Classification.

**Source/Content:** The Localizer/MLS/GLS Category/Classification will be derived from official government sources and will be indicated by a value from the table below.

| Category/Classification | Definition |
|---|---|
| 0 | ILS Localizer Only, No Glideslope |
| 1 | ILS Localizer/MLS/GLS Category I |
| 2 | ILS Localizer/MLS/GLS Category II |
| 3 | ILS Localizer/MLS/GLS Category III |
| I | IGS Facility |
| L | LDA Facility with Glideslope |
| A | LDA Facility, no Glideslope |
| S | SDF Facility with Glideslope |
| F | SDF Facility, no Glideslope |

**Used On:** Runway, Localizer, MLS and MLS Continuation Records, GLS Record.
**Length:** 1 character
**Character Type:** Alpha/Numeric
</details>

<details>
<summary>5.82 - Waypoint Usage</summary>

**Definition/Description:** The waypoint usage field is employed to indicate the airway structure in which the waypoint is utilized.

**Source/Content:**

| Usage Content | Record Column 30 | Record Column 31 |
|---|---|---|
| HI and LO Altitude Airway | B | |
| HI Altitude Airway | H | |
| LO Altitude Airway | L | |
| HI Altitude RNAV Airway | R | |
| Terminal Use only | Blank | Blank |

**Used On:** Enroute (EA) waypoint records
**Length:** 2 characters
**Character Type:** Alpha
</details>

<details>
<summary>5.83 - To FIX</summary>

**Definition/Description:** The Company Route and Preferred Route "To Fix" field is used to terminate the route referenced in the SID/STAR/APCH/AWY field (5.78), or terminate a "Direct" segment or start an "Initial" segment when no SID/STAR/APCH/AWY is referenced.

**Source/Content:** For Company Route records the field will contain Enroute Waypoint, Terminal Waypoint, VHF NAVAID, NDB NAVAID, Terminal NDB NAVAID, Airport or Runway Identifier. The customer will define where a particular route segment is to terminate. For Preferred Route records, the field will contain Enroute Waypoint, Terminal Waypoint, VHF NAVAID, NDB NAVAID or Terminal NDB NAVID, Airport Identifier.

**Used On:** Company Route and Preferred Route Records
**Length:** Company Route - 6 characters max; Preferred Route - 5 characters max.
**Character Type:** Alpha/numeric
**Examples:** SHARP, BHM, DEN43, KDEN, RW35R
</details>

<details>
<summary>5.84 - RUNWAY TRANS</summary>

**Definition/Description:** This field is used to identify the desired runway transition of the applicable SID or STAR. It is used to link directly to the SID/STAR procedure records depending on the Company Route record "VIA" field (5.77) and whether or not the SID/STAR has explicit runway transitions.

**Source/Content:** If the applicable SID/STAR has explicit runway transitions then this field uniquely identifies the desired runway transition. If no runway transition is desired, the field is blank. If the applicable SID/STAR does not have explicit runway transitions this field is always non-blank and exactly matches the "TRANS IDENT" field of the SID/STAR procedure records.

VIA field contains "SDY" or "STY": In this situation the field contents are defined exactly as stated above (VIA field = "SID" or "STR") except that the field is always non-blank. This field is blank for all other contents of the VIA field.

**Used On:** Company Route Records
**Length:** 5 characters
**Character Type:** Alpha/Numeric
**Examples:** RW08L, ALL, Blank
</details>

<details>
<summary>5.85 - ENRT TRANS</summary>

**Definition/Description:** This field is used to identify the desired enroute transition of the applicable SID or STAR. It can also be used to identify the desired approach transition of an approach.

**Source/Content:**

VIA field contains "SID" or STR": This field uniquely identifies the desired SID/STAR enroute transition. If no enroute transition is desired, the field is blank.

VIA field contains "SDE" or "STE": In this situation the field contents are defined exactly as stated above (VIA field - "SID" or "STR") except that the field is always non-blank.

VIA field contain "APP": This field uniquely identifies the desired approach transition. If no approach transition is desired, the field is blank.

The field is blank for all other contents of the VIA field.

**Used On:** Company Route Records
**Length:** 5 characters
**Character Type:** Alpha/Numeric
**Examples:** ETS, KEENE, DEN
</details>

<details>
<summary>5.86 - Cruise Altitude</summary>

**Definition/Description:** This field will be used to establish an Enroute Cruise Altitude. It will be entered on Company Route records as specified by the customer.

**Source/Content:** The customer will supply the Cruise Altitude in feet or flight level.

**Used On:** Company Route Records
**Length:** 5 characters
**Character Type:** Alpha/Numeric
**Examples:** 10000, 15000, FL090, FL240
</details>

<details>
<summary>5.87 - Terminal/Alternate Airport (TERM/ALT ARPT)</summary>

**Definition/Description:** This field has two uses depending on the "VIA" field and File Code for "To Fix." For "VIA" field content of "ALT" this field will contain the Alternate Airport Ident for this Company Route. If the file code for "To Fix" contains "P," this field will contain the Airport Ident for REGN CODE (Section 5.41) of Terminal Waypoints (PC records) and Runway (PG records).

**Source/Content:** See Section 5.6, Airport ICAO Identifier.

**Used On:** Route Records
**Length:** 4 characters
**Character Type:** Alpha/Numeric
**Examples:** KDEN, EDDF
</details>

<details>
<summary>5.88 - Alternate Distance (ALT DIST)</summary>

**Definition/Description:** This field is used to supply the distance in nautical miles from the "To Airport/Fix" to the "ALT ARPT".

**Source/Content:** Values for this field will be supplied by the customer and must be equal to or greater than the great circle distance from the destination airport/fix to the alternate airport.

**Used On:** Company Route Records
**Length:** 4 characters
**Character Type:** Numeric
**Examples:** 052, 0011, 0123
</details>

<details>
<summary>5.89 - Cost Index</summary>

**Definition/Description:** The Cost Index field is used to define the relative value of fuel-related costs and time-related costs for a particular route.

**Source/Content:** Source will be by customer airline.

**Used On:** Company Route Records
**Length:** 3 characters
**Character Type:** Numeric
**Examples:** 001, 011, 999
</details>

<details>
<summary>5.90 - ILS/DME Bias</summary>

**Definition/Description:** This field is used to specify the DME offset.

**Source/Content:** The field contains a 2-digit bias term in nautical miles and tenths of a nautical mile with the decimal point suppressed. Field is blank for unbiased DME's.

**Used On:** VHF NAVAID Records containing ILS/DME or MLS/DME Facilities
**Length:** 2 characters
**Character Type:** Numeric
**Examples:** 13, 91
</details>

<details>
<summary>5.91 - Continuation Record Application Type (APPL)</summary>

**Definition/Description:** This field indicates specific application of this continuation record.

**Source/Content:**

| Field Content | Application |
|---|---|
| P | Flight Planning |
| S | Simulation |

**Used On:** Continuation records
**Length:** One character
**Character Type:** Alpha
</details>

<details>
<summary>5.92 - Facility Elevation (FAC ELEV)</summary>

**Definition/Description:** This "Elevation" field defines the elevation of the VOR, NDB, ILS Marker, Airways Marker and Airport Communications stations.

**Source/Content:** Facility elevations specified in official government publications are entered into this field in feet with respect to MSL. When the elevation is below MSL, the first column of the field contains a minus (-) sign.

**Used On:** ILS Marker, Airways Marker, Enroute/Airport Communications primary records. VHF Navaids and NDB Navaids continuation records.
**Length:** 5 characters
**Character Type:** Alpha/Numeric
**Examples:** 00530, -0014
</details>

<details>
<summary>5.93 - Facility Characteristics (FAC CHAR)</summary>

**Definition/Description:** The "Facility Characteristics" field identifies the characteristics of the NAVAID facility.

**Source/Content:**

| Facility | Columns | Code | Description |
|---|---|---|---|
| VHF NAVAID, ILS & MLS | 28-32 | S | Synchronous |
| | | A | Asynchronous |
| | | U | Unknown |
| VHF NAVAID, NDB NAVAID and Locator | | Y | Voice Ident |
| | | N | No Voice Ident |
| | | U | Undefined |
| NDB NAVAID | | 4 | Type of emission 400H (Note 1) |
| | | 1 | Type of emission 1020H (Note 1) |
| | | 2 | Repetition Rate (Note 2) |
| ILS DME Location | | L | Colocated with Localizer (Note 3) |
| | | G | Colocated with Glide Slope |
| | | Blank | Not co-located with Localizer or Glide Slope |
| ILS Back Course | | Y | Usable |
| | | N | Unusable |
| | | R | Restricted |
| | | U | Undefined |
| MLS, DME or DME/P Location | | A | Colocated with Azimuth |
| | | E | Colocated with Elevation |
| | | N | Not Colocated with Azimuth or Elevation |
| MLS Approach Azimuth Scan Rate | | 4 | (Note 4) |

Note 1: 0=A0, 1=A1, 2=A2

Note 2: Enter number of occurrences per minute if known. Leave blank if not known.

Note 3: Colocated means that the latitudes and longitudes of the two facilities differ by no more than 1 arc second.

Note 4: Where a high-rate approach azimuth guidance is available, enter "H," otherwise leave blank.

COMMENTARY: The NDB emission designators set forth in Note 1 above are being replaced with the new designators shown in the equivalency table below as the result of action taken at the 1979 ITU World Administrative Radio Conference.

| Present Designator | New Designator | Description |
|---|---|---|
| A0/NON | A1A | Unmodulated Carrier |
| A1 | A1B | Carrier keyed, bandwidth less than 0.1 kHz |
| A2 | A2A | Tone keyed modulation, bandwidth greater than 0.1 kHz |

**Used On:** ILS Marker Primary records, VHF Navaid, NDB Navaid and ILS/MLS continuation records
**Length:** 5 characters
**Character Type:** Alpha/Numeric
</details>

<details>
<summary>5.94 - True Bearing (TRUE BRG)</summary>

**Definition/Description:** The "Magnetic Bearing" for ILS localizer, MLS Azimuth, MLS Back Azimuth and Runway records is given in the primary record. This field allows the true bearing to be entered independently of the magnetic variation.

**Source/Content:** True Bearings are entered into the field in degrees, tenths of a degree and hundredths of a degree, with the decimal point suppressed. See Section 5.95 for source description.

**Used On:** ILS Continuation, MLS Continuation and Runway Continuation records
**Length:** 5 characters
**Character Type:** Numeric
**Examples:** 19000, 23021, 06050
</details>

<details>
<summary>5.95 - Government Source (SOURCE)</summary>

**Definition/Description:** The content of the source field indicates whether the "True Bearing" is derived from official government sources or from other sources.

**Source/Content:** The field contains "Y" when the "True Bearing" is derived from official government sources and "N" when it is derived from other sources.

**Used On:** ILS, MLS, MLS continuation and runway continuation records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.96 - Glide Slope Beam Width (GS BEAM WIDTH)</summary>

**Definition/Description:** The "Glide Slope Beam Width" field specifies the glide path beam width of the Glide Slope defined in the record.

**Source/Content:** Glide Slope beam widths from official government sources are entered into this field in degrees, tenths of a degree and hundredths of a degree with the decimal point suppressed.

**Used On:** ILS continuation records
**Length:** 3 characters
**Character Type:** Numeric
**Examples:** 140, 180, 200
</details>

<details>
<summary>5.97 - Touchdown Zone Elevation (TDZE)</summary>

**Definition/Description:** The "Touchdown Zone Elevation" is the highest elevation in the first 3,000 feet of the landing surface beginning at the threshold.

**Source/Content:** Touchdown zone elevations from official government sources will be used when available. If official source is not available, the runway threshold elevation will be entered. If the runway threshold elevation is not available, the Airport reference point elevation will be entered. (See TDZE Location, Section 5.98) The elevation will be entered in feet, to a resolution of 1 foot, with respect to MSL. For below MSL elevations, the first character of the field is a minus (-) sign.

**Used On:** Runway continuation records
**Length:** 5 characters
**Character Type:** Alpha/Numeric
**Examples:** 02171, 05230, -0142
</details>

<details>
<summary>5.98 - TDZE Location (LOCATION)</summary>

**Definition/Description:** The content of the "TDZE Location" field indicates whether the TDZ elevation was obtained from official government sources or from other sources.

**Source/Content:** The field will contain a "T" for official source or a "L" if the landing threshold elevation is used, or an "A" if the airport elevation is used.

**Used On:** Runway continuation records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.99 - Marker Type (MKR TYPE)</summary>

**Definition/Description:** The "Marker Type" field defines the type of marker.

**Source/Content:** The field contains the following information.

| Type of Facility | Record Column 18 | Record Column 19 | Record Column 20 |
|---|---|---|---|
| Inner Marker | I | M | |
| Middle Marker | M | M | |
| Outer Marker | O | M | |
| Back Marker | B | M | |
| Locator at Marker | L | | |

**Used On:** Airport Localizer Marker records
**Length:** 3 characters
**Character Type:** Alpha
</details>

<details>
<summary>5.100 - Minor Axis Bearing (MINOR AXIS TRUE BRG)</summary>

**Definition/Description:** The "Minor Axis Bearing" field indicates the true bearing of the minor axis of marker beacons.

**Source/Content:** This field will contain the true bearing in degrees and tenths of a degree, with the decimal point suppressed.

**Used On:** Airport Localizer Marker records
**Length:** 4 characters
**Character Type:** Numeric
**Examples:** 0900, 2715
</details>

<details>
<summary>5.101 - Communications Type (COMM TYPE)</summary>

**Definition/Description:** The "Communications Type" field specifies the type of communication unit contained in the record.

**Source/Content:** The field will contain one of the following entries.

| Field Content | Description | Airport Comm Only | Heliport Comm Only | Enroute Comm Only | Both Comm Type |
|---|---|---|---|---|---|
| ACC | Area Control Center | | | | X |
| ACP | Airlift Command Post | X | | | |
| APP | Approach Control | X | | | |
| ARR | Arrival Control | X | | | |
| ATI | Automatic Terminal Info Service (ATIS) | X | | | |
| AWO | Automatic Weather Observing Service (AWOS) | X | | | |
| CLD | Clearance Delivery | X | | | |
| CPT | Clearance, Pre-Taxi | X | | | |
| CTA | Control Area (Terminal) | X | | | |
| CTL | Control | | | X | |
| DEP | Departure Control | X | | | |
| DIR | Director (Approach Control Radar) | X | | | |
| EMR | Emergency | | | X | |
| FSS | Flight Service Station | | | X | |
| GND | Ground Control | X | | | |
| GTE | Gate Control | X | | | |
| HEL | Helicopter Frequency | | X | | |
| INF | Information | | | X | |
| MUL | Multicom | | | X | |
| OPS | Operations | | X | | |
| RDO | Radio | | | X | |
| RDR | Radar | | | X | |
| RFS | Remote Flight Service Station (RFSS) | | | X | |
| RMP | Ramp/Taxi Control | X | | | |
| RSA | Airport Radar Service Area (ARSA) | X | | | |
| TCA | Terminal Control Area (TCA) | X | | | |
| TMA | Terminal Control Area (TMA) | X | | | |
| TML | Terminal | X | | | |
| TRS | Terminal Radar Service Area (TRSA) | X | | | |
| TWE | Transcriber Weather Broadcast (TWEB) | X | | | |
| TWR | Tower, Air Traffic Control | X | | | |
| UAC | Upper Area Control | | | X | |
| UNI | Unicom | X | | | |
| VOL | Volmet | | | X | |

**Used On:** Enroute, Airport and Heliport Communications
**Length:** 3 characters
**Character Type:** Alpha
</details>

<details>
<summary>5.102 - Radar (RADAR)</summary>

**Definition/Description:** The "Radar" field indicates whether or not the communications unit has access to information derived from primary or secondary radar and can use that information in fulfilling their assigned tasks.

**Source/Content:** The availability or radar capability will be derived from official government source documentation. If the communications unit has radar capabilities, the field will contain the character "R". If no capability exists, the field will contain the character "N".

**Used On:** Enroute, Airport and Heliport Communications records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.103 - Communications Frequency (COMM FREQ)</summary>

**Definition/Description:** The "Communications Frequency" field specifies a frequency for the facility identified in the "Communications Type" (5.101) field.

**Source/Content:** Frequencies are derived from official government sources. HF frequencies are provided in 10 thousands, thousands, hundreds, tens and units of kilohertz (kHz) with trailing zeros in the tenths and hundreds position. VHF frequencies are provided in hundreds, ten, units, tenths, hundredths and thousandths of megahertz (MHz). UHF frequencies are provided in hundreds, ten, units, tenths and hundredths of megahertz (MHz). Decimal points are always suppressed.

**Used On:** Enroute, Airport and Heliport Communications records
**Length:** 7 characters
**Character Type:** Numeric
**Examples:** HF Frequencies - 0309500, 1794600; VHF Frequencies - 0123750, 0119700, 0126125; UHF Frequencies - 0028785, 0025350, 0026700
</details>

<details>
<summary>5.104 - Frequency Units (FREQ UNIT)</summary>

**Definition/Description:** The "Frequency Units" field will designate the frequency spectrum area for the frequency in the "Communications Frequency" (5.103) field.

**Source/Content:** This field contains the follow information.

| Field Content | Description |
|---|---|
| H | High Frequency (3000 kHz - 30,000 kHz) |
| V | Very High Frequency (30,000 kHz - 200 MHz) |
| U | Ultra High Frequency (200 MHz - 3000 MHz) |

**Used On:** Enroute, Airport and Heliport Communications records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.107 - ATA/IATA Designator (ATA/IATA)</summary>

**Definition/Description:** The "ATA/IATA" field contains the Airport/Heliport ATA/IATA designator code to which the data contained in the record relates.

**Source/Content:** The content of this field should be derived from IATA Reservations Manual Part II, IATA Resolution 763/Location Identifiers.

**Used On:** Airport and Heliport records
**Length:** 3 characters
**Character Type:** Alpha
**Examples:** DEN, LHR, JFK
</details>

<details>
<summary>5.108 - IFR Capability (IFR)</summary>

**Definition/Description:** The "IFR Capability" field indicates if the Airport/Heliport has any published Instrument Approach Procedures.

**Source/Content:** The field contains "Y" if there is an Official Government Instrument Approach Procedure published, otherwise the field will contain "N". (Note: The presence of "Y" in this field does not necessarily imply that the published instrument approach is coded in the data base.)

**Used On:** Airport and Heliport records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.109 - Runway Width (WIDTH)</summary>

**Definition/Description:** The width of the runway identified in the "Runway Identifier" field is specified in the "Runway Width" field.

**Source/Content:** Runway widths derived from Official Government Sources are entered into the field in feet, with a resolution of one foot. For runways of variable width, the minimum width encountered over the runway length will be entered.

**Used On:** Runway records
**Length:** 3 characters
**Character Type:** Numeric
**Examples:** 150, 300, 075
</details>

<details>
<summary>5.110 - Marker Ident (MARKER IDENT)</summary>

**Definition/Description:** The "Marker Ident" field contains a unique computer ident assigned to each enroute marker.

**Source/Content:** A unique identifier will be created for each enroute marker since such idents are not designated by official sources. Marker idents will be established using the 2-character ICAO code followed by two numeric digits assigned to keep markers unique within a given ICAO region.

**Used On:** Enroute marker records
**Length:** 4 characters
**Character Type:** Alpha/Numeric
**Examples:** EG01, EG02, K101, K102
</details>

<details>
<summary>5.111 - Marker Code (MARKER CODE)</summary>

**Definition/Description:** The "Marker Code" field contains the coded ident that provides an aural and visual indication of station passage in the cockpit. The code shall be keyed so as to transmit dots or dashes, or both, in an appropriate sequence on a radio frequency of 75 MHz. The frequency of the modulating tone is 3000 Hz.

**Source/Content:** The field contains the morse code ident (dots and dashes) derived from official government sources.

**Used On:** Enroute marker records
**Length:** 4 characters
**Character Type:** Alpha
**Examples:** .-., . . . ., - - - -
</details>

<details>
<summary>5.112 - Marker Shape (SHAPE)</summary>

**Definition/Description:** The "Shape" field defines the radiation pattern of an airways marker as being either "bone" or "elliptical."

**Source/Content:** The field contains the shape of the marker derived from official government sources when available. The character "B" will designate the "bone" shape and the character "E" will designate the elliptical shape. "E" will be entered when the source does not supply shape information.

**Used On:** Enroute airways marker records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.113 - High/Low (HIGH/LOW)</summary>

**Definition/Description:** The "High/Low" field indicates the power of the enroute marker.

**Source/Content:** The field contains the power derived from official government sources. The character "L" indicates low power for use at low altitudes. The character "H" indicates high power for general use.

**Used On:** Enroute marker records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.114 - Duplicate Indicator (DUP IND)</summary>

**Definition/Description:** The "Duplicate Identifier" field is used to further define holding patterns when official government source has designated more than one Holding Pattern on a Navaid or Waypoint.

**Source/Content:** Holding Patterns are derived from official government sources documents. That documentation will normally specify the airspace structure in which the holding is to be used. That documentation may also designate more than one Holding Pattern for a single Navaid or Waypoint. This field will contain detail on airspace structure and multiple designations. More than one holding is designated on a single "fix" when one or more of the following elements differ for holdings within the same airspace structure: Inbound Holding Course, Turn Direction, Altitude, Leg Length or Leg Time, and Holding Speed.

If only one Holding Pattern is designated for a "fix" and the airspace structure in which that holding is to be used is not defined, the field will contain "00". If only one Holding Pattern is designated for a "fix" and the airspace structure in which that holding is to be used is defined or if the same holding is designated for more than one airspace structure, the first position of the "Duplicate Indicator" will contain a digit of 1 through 6 and the second position will contain a zero. If more than one holding is designated for a single "fix" in one type of airspace structure, the first position will contain a digit of 1 through 6 and the second position will contain a digit of 1 through 9, depending on the number of holdings on that "fix" within that airspace structure.

If multiple holdings are designated in official source documents for a single "fix" and the airspace structure is not defined for all holdings, those with "undefined airspace structure" will carry the digit 7 in position one and a digit of 0 through 9 in position two.

MULTIPLE HOLDING PATTERNS:

| Holding Pattern Airspace | Duplicate Indicator Position One | Duplicate Indicator Position Two |
|---|---|---|
| Undefined (None Defined) | 0 | See Note 1 |
| High Altitude | 1 | See Note 1 |
| Low Altitude | 2 | See Note 1 |
| SID | 3 | See Note 1 |
| STAR | 4 | See Note 1 |
| Approach | 5 | See Note 1 |
| Missed Approach | 6 | See Note 1 |
| Undefined (with other defined) | 7 | See Note 1 |

Note 1: If there is only one holding pattern on a given fix within an airspace structure, position 2 will contain a "0". For additional (multiple) holdings on that same fix within the same airspace structure, position 2 will be incremented by 1, e.g. "0" for the first "1" for the second, etc.

**Used On:** Holding Pattern Records
**Length:** 2 characters
**Character Type:** Numeric
**Examples:** 00, 10, 61, 32
</details>

<details>
<summary>5.116 - FIR/UIR Identifier (FIR/UIR IDENT)</summary>

**Definition/Description:** The "FIR/UIR Identifier" field identifies the Flight Information Region and Upper Information Region of airspace with defined dimensions within which Flight Information Service and Alerting Service are provided. The Identifier is for the controlling Area Control Center or Flight Information Center.

**Source/Content:** FIR/UIR Identifiers will be derived from official government sources. This field contains the four character identifier assigned to the airspace. For those areas charted as "NO FIR," the identifier field will contain "XX plus a two digit numeric."

When used on Flight Planning Continuation records, the entry will be related to the altitude structure. For records that are classed or designated as high altitude, the FIR field will be blank. For areas assigned a FIR identifier only that is valid for both the low altitude and the high altitude structure, the UIR field will be blank. For detail records classed or designated as low altitude and high altitude, both the FIR and the UIR identifier will be entered.

**Used On:** FIR/UIR, VHF NAVAID, NDB NAVAID, Enroute, Terminal Waypoint, Airport Flight Planning Continuation and Heliport records
**Length:** 4 characters
**Character Type:** Alpha
**Examples:** DAAG, SGAS, XX02
</details>

<details>
<summary>5.117 - FIR/UIR Indicator (IND)</summary>

**Definition/Description:** The "FIR/UIR Identifier" field may contain the identifier of a FIR, UIR or combined FIR/UIR. This field indicates which one of these records is an element.

**Source/Content:**

| Type | Field Entry |
|---|---|
| FIR | F |
| UIR | U |
| Combined FIR/UIR | B |

**Used On:** FIR/UIR and Enroute Communications records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.118 - Boundary Via (BDRY VIA)</summary>

**Definition/Description:** The "Boundary VIA" defines the path of the boundary from the position identified in the record to the next defined position.

**Source/Content:** The path of the boundary will be determined from official government sources or the rule listed below and the "Boundary VIA" will be selected from the table below.

| Field Content | Description |
|---|---|
| A | Arc by edge |
| C | Circle |
| G | Great Circle |
| H | Rhumb Line |
| L | Counter Clockwise ARC |
| R | Clockwise ARC |
| E | End of description, return to origin point |

Application Rules:

1. Special Use Airspace designated as following rivers, country, state or other political boundaries will be averaged in coding by using a series of straight lines so that no path will be greater than two miles from the actual boundary. The Boundary VIA will be "G".
2. If there is a named waypoint on an airway which crossed an irregular FIR/UIR boundary, the waypoint entry coordinates will be used to define a point in the path defining that FIR/UIR boundary. The Boundary VIA will appropriate to the path definition.
3. Paths that follow lines of latitude will be coded with a Boundary Via of "H". Paths that follow lines of longitude may be coded with a Boundary Via of "G" or "H". Consistent use of one or the other within a single airspace is desired.
4. Other than for lines of latitude and longitude, the Boundary VIA of "H" shall only be used when specifically stated in the official government source. If not stated as "Rhumb Line" or not along latitude/longitude, all straight lines will be coded as "G".

Note: Refer to Figure 5-12 for sample coding of Boundary VIA Codes.

**Used On:** Controlled Airspace, FIR/UIR, and Restrictive Airspace records
**Length:** 2 characters
**Character Type:** Alpha
</details>

<details>
<summary>5.119 - Arc Distance (ARC DIST)</summary>

**Definition/Description:** The "Arc Distance" field is used to define the distance in nautical miles from the "Arc Origin" position to the arc defining the lateral boundary of a FIR/UIR or Restrictive Airspace.

**Source/Content:** ARC distances should be derived from official government sources when available, in nautical miles and tenths of nautical mile, with the decimal point suppressed. The field will be entered only when "Boundary Via" is "A," "C," "L," or "R".

**Used On:** FIR/UIR, Restrictive Airspace, and Controlled Airspace records
**Length:** 4 characters
**Character Type:** Numeric
**Examples:** 0080, 0150, 1000
</details>

<details>
<summary>5.120 - Arc Bearing (ARC BRG)</summary>

**Definition/Description:** The "Arc Bearing" field contains the true bearing from the "Arc Origin" position to the beginning of the arc.

**Source/Content:** Arc bearings should be derived from official government sources when available. The field contains true bearing in degrees and tenths of degree, with the decimal point suppressed. The field will only be entered when Boundary Via is "A," "C," "L" or "R".

**Used On:** FIR/UIR, Restrictive Airspace, and Controlled Airspace records
**Length:** 4 characters
**Character Type:** Numeric
**Examples:** 0900, 1800, 3450
</details>

<details>
<summary>5.121 - Lower/Upper Limit</summary>

**Definition/Description:** Special Use Airspace is described by both lateral and vertical boundaries. The "Lower/Upper Limit" fields contain the lower and upper limits of the FIR/UIR or Restrictive Airspace being described.

**Source/Content:** Limits for the special use airspace should be derived from official government sources. The field may contain altitude (all numerics), flight levels (alpha/numerics) or an all alpha entry (see examples). The flight level entry will contain the alpha characters "FL" followed by the altitude in hundreds of feet. These fields will be entered on the first record only of each FIR/UIR or Restrictive Airspace being described.

**Used On:** FIR/UIR, Restrictive Airspace, and Controlled Airspace records
**Length:** 5 characters
**Character Type:** Alpha/Numeric
**Examples:** All numeric: 05000, 25000; Alpha/numeric: FL245, FL450; All alpha: NOTSP (for Not Specified), UNLTD (for unlimited), GND (for Ground), MSL (for Mean Sea Level), NOTAM (for Restrictive Airspace only)
</details>

<details>
<summary>5.122 - FIR/UIR ATC Reporting Units Speed (RUS)</summary>

**Definition/Description:** The "FIR/UIR ATC Reporting Units Speed" is used to indicate the units of measurement concerning True Air Speed used in the specific FIR/UIR to fulfill the requirements of ICAO flight plan.

**Source/Content:** FIR/UIR Reporting Units should be derived from official government publications. The field will be entered on the first record only for each FIR/UIR identifier.

| Reporting Units | Field Entry |
|---|---|
| Not specified | 0 |
| TAS in Knots | 1 |
| TAS in Mach | 2 |
| TAS in Kilometers/hr | 3 |

**Used On:** FIR/UIR records
**Length:** 1 character
**Character Type:** Numeric
</details>

<details>
<summary>5.123 - FIR/UIR ATC Reporting Units Altitude (RUA)</summary>

**Definition/Description:** The "FIR/UIR ATC Reporting Units Altitude" field is used to indicate the units of measurement concerning the altitude used in the specific FIR/UIR to fulfill the requirements of ICAO flight plan.

**Source/Content:** FIR/UIR Reporting Units should be derived from official government publications. The field will be entered on the first record only for each FIR/UIR identifier.

| Reporting Units | Field Entry |
|---|---|
| Not specified | 0 |
| ALT in Flight Level | 1 |
| ALT in Meters | 2 |
| ALT in Feet | 3 |

**Used On:** FIR/UIR records
**Length:** 1 character
**Character Type:** Numeric
</details>

<details>
<summary>5.124 - FIR/UIR Entry Report (ENTRY)</summary>

**Definition/Description:** The "FIR/UIR Entry Report" field is used to indicate whether an entry report on ICAO flight plan is required for that specific FIR/UIR.

**Source/Content:** FIR/UIR Entry Report should be derived from official government publications. "Y" in this field indicates Entry Report is required, "N" in this field indicates no Entry Report is required. The field will be entered on the first record only for each FIR/UIR identifier.

**Used On:** FIR/UIR records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.125 - FIR/UIR Name</summary>

**Definition/Description:** The "FIR/UIR Name" field contains the official name of the controlling agency of the FIR/UIR of which this record is an element.

**Source/Content:** The FIR/UIR name will be derived from official publications. The areas without a specific "FIR/UIR" designation will be labeled "NO FIR".

**Used On:** FIR/UIR records
**Length:** 25 characters
**Character Type:** Alpha/numeric
**Examples:** ACCRA, FIR, ASUNCION FIR/UIR, NO FIR
</details>

<details>
<summary>5.126 - Restrictive Airspace Name</summary>

**Definition/Description:** The "Restrictive Airspace Name" field will contain the name of the restrictive airspace when assigned.

**Source/Content:** Names will be derived from official government sources. The name, if assigned, will be entered in the first record only. If source does not assign a name, this field may be blank.

**Used On:** Restrictive Airspace records
**Length:** 30 characters
**Character Type:** Alpha/numeric
**Examples:** RANDOLPH ONE MOA, SAMBURU GAME RESERVE
</details>

<details>
<summary>5.127 - Maximum Altitude (MAX ALT)</summary>

**Definition/Description:** The "Maximum Altitude" field is used to indicate the maximum altitude allowed.

**Source/Content:** Maximum altitudes should be derived from official government publications describing the upper limit of the airway in feet or flight level.

**Used On:** Enroute Airway, Holding Pattern and Preferred Route records
**Length:** 5 characters
**Character Type:** Alpha/numeric
**Examples:** All numeric: 17999, 08000; Alpha/numeric: FL100, FL450; All alpha: UNLTD (for unlimited)
</details>

<details>
<summary>5.128 - Restrictive Airspace Type (REST TYPE)</summary>

**Definition/Description:** The "Restrictive Airspace Type" field is used to indicate the type of Airspace in which the flight of aircraft is prohibited or restricted. The restriction may be continuous or specified for certain times.

**Source/Content:** The "Restrictive Airspace Type" should be derived from official government publications.

| Type | Field Entry |
|---|---|
| Alert | A |
| Caution | C |
| Danger | D |
| Military Operations Area | M |
| Prohibited | P |
| Restricted | R |
| Training | T |
| Warning | W |
| Unspecified or Unknown | U |

**Used On:** Restrictive Airspace and Enroute Airway Flight Planning Continuation records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.129 - Restrictive Airspace Designation</summary>

**Definition/Description:** The "Restrictive Airspace Designation" field contains the number or name that uniquely identifies the restrictive airspace.

**Source/Content:** The identifiers will be derived from official government sources. The field will contain a numeric number, or when designation is by name this field will contain the name up to 10 characters. When name is longer than 10 characters, the 10th position will contain an asterisk indicating the name field should be used for the full designator.

| Charted Designator | ICAO | Type | Rest. Desig. |
|---|---|---|---|
| RJ(R)-116 | RJ | R | 116 |
| R-2524 | K2 | R | 2524 |
| Crystal MOA | K4 | M | Crystal |
| Randolph MOA One | K4 | M | Randolph* |

**Used On:** Restrictive Airspace and Enroute Airway Flight Planning Continuation records
**Length:** 10 characters
**Character Type:** Alpha/numeric
</details>

<details>
<summary>5.130 - Multiple Code (MULTI CD)</summary>

**Definition/Description:** The "Multiple Code" field will be used to indicate Restrictive Airspace Areas or MSA Centers having the same designator but subdivided or differently divided by lateral and/or vertical detail.

**Source/Content:** This field will be used when official government publications for Restrictive Airspace divides an area with the same designator into different areas of Activation, altitude or other defining characteristics. For MSA Centers, this provides different sectorization and/or altitudes for the MSA published with the same center. The field will contain an alpha character uniquely identifying each area or MSA. The first record affected could contain the character "A" and multiple primary records could contain the character "B," "C," "D," etc., as required.

**Used On:** Controlled Airspace, Restrictive Airspace, Airport and Heliport MSA Center, Airport and Heliport SID/STAR/Approach and Enroute Airway Flight Planning Continuation Records.
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.131 - Time Code (TIME CD)</summary>

**Definition/Description:** When used on the Primary Record of the possible record types, with the exception of Enroute Airway Restriction Records, this field is used to identify that the record in question is continuous or the times are other than continuous and are shown in a Continuation Record. When used on a Continuation Record, other than the Enroute Airway Restriction Records, this field is used to indicate how the "Time of Operation Fields" are to be interpreted. When used on Enroute Airway Restriction Primary and Continuation Records, this field identifies either a continuous situation or a non-continuous situation, the detail for which is contained in the same record as the Time Code.

**Source/Content:** Active times are derived from official government source. The field will contain an alpha character for which an associated description has been defined as indicated in the tables below.

PRIMARY RECORDS:

| Field Entry | Description |
|---|---|
| C | Active Continuously, including holidays |
| H | Active Continuously, excluding holidays |
| N | Active Non-Continuously, Refer to Continuation Record |
| Blank | Active times announced by NOTAM |

CONTINUATION RECORDS:

| Field Entry | Description |
|---|---|
| H | Active times are provided in Time of Operation format and exclude holidays |
| N | Activation Times are too complex for Time of Operation format and are provided in Note Form |
| T | Active times are provided in Time of Operation format and include holidays |

PRIMARY AND CONTINUATION RECORDS:

| Field Entry | Description |
|---|---|
| C | Active Continuously, including holidays |
| H | Active Continuously, excluding holidays |
| S | Active times are provided in Time of Operation format and exclude holidays |
| T | Active times are provided in Time of Operation format and include holidays |

**Used on:** Enroute Airway Restriction Primary and Continuation Records
**Length:** One character
**Character Type:** Alpha
</details>

<details>
<summary>5.132 - NOTAM</summary>

**Definition/Description:** Restrictive Airspace areas may not have established active times and are activated by NOTAM or may be active by NOTAM in addition to established times.

**Source/Content:** Active times by NOTAM will be derived from official government source. When used on primary records, the area is active only by NOTAM and there will be no continuation record. When used on continuation records, the area is active by NOTAM in addition to the established times. The field will contain the alpha character "N" to indicate either condition, otherwise the field will be blank.

**Used On:** Controlled Airspace, Restrictive Airspace and Restrictive Airspace Continuation records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.133 - Unit Indicator (UNIT IND)</summary>

**Definition/Description:** Restrictive Airspace lower and upper limits are specified as "above mean sea level" (MSL) or "above ground level" (AGL). This field permits the unit of measurement to be indicated.

**Source/Content:** The units of lower and upper limits are derived from official government source. The alpha character "M" will indicate MSL and the alpha character "A" will indicate AGL.

**Used On:** Controlled Airspace, Restrictive Airspace records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.134 - Cruise Table Identifier (CRSE TBL IDENT)</summary>

**Definition/Description:** A standard cruising level table is established by ICAO and is to be observed except when, on the basis of regional air navigation agreements, a modified table of cruising levels is prescribed for use. This field permits the enroute airway record to identify the Cruise Table record that is to be used for cruise levels.

**Source/Content:** Cruise Levels will be derived from official government sources. For the standard ICAO cruise table this field will contain the alpha characters "AA". For those countries not using the standard ICAO table and having a modified table this field will contain the alpha characters "BB," "CC," etc. If a country uses the standard ICAO table or a Modified table but indicates that an airway or portion of an airway is to be flown opposite of the cruise table, the field will contain alpha/numeric characters that identify the table to be used.

| Field Entry | Description |
|---|---|
| AA | ICAO standard cruise table |
| AO | Exception to ICAO cruise table |
| BB - ZZ | Modified cruise table |
| BO - ZO | Exception to modified cruise table |

**Used On:** Enroute Airway, FIR/UIR, Cruise Table and Flight Planning Arrival/Departure Data Records
**Length:** 2 characters
**Character Type:** Alpha/numeric
</details>

<details>
<summary>5.138 - Time Indicator (TIME IND)</summary>

**Definition/Description:** The "Time Indicator" field is used to indicate whether the times shown in the "Time of Operations" field(s) are Local Time, Daylight Savings Time or Universal Coordinated Time.

**Source/Content:** Time contained in the affected record(s) is derived from official government sources. The "Time Indicator" will qualify those source derived times as indicated in the following table:

| Field Entry | Description |
|---|---|
| T | Times codes are Local Time |
| S | Times codes are to be adjusted for Daylight Savings Time |
| Blank | Times shown are Universal Coordinated Time (UTC) |
</details>

<details>
<summary>5.140 - Controlling Agency</summary>

**Definition/Description:** Some "Restrictive Airspace" areas are designated joint use and IFR operations in the area may be authorized by the controlling agency when it is not being utilized by the using agency.

**Source/Content:** The name of the Controlling Agency should be derived from official government sources and will be shown on the first record only. If no Controlling Agency is specified the field may be blank.

**Used On:** Controlled Airspace, Restrictive Airspace Continuation record
**Length:** 25 characters
**Character Type:** Alpha/numeric
**Examples:** LAX, ARTCC, Lumpur ACC, Butterworth APP
</details>

<details>
<summary>5.141 - Starting Latitude</summary>

**Definition/Description:** The Grid MORA Table will contain records describing the MORA for each Latitude and Longitude block. Each record will contain thirty blocks and the "Starting Latitude" field defines the lower left corner for the first block of each record.

**Source/Content:** The "Starting Latitude" will be determined when the record is assembled.

**Used On:** Grid Mora record
**Length:** 3 characters
**Character Type:** Alpha/numeric
**Examples:** N00, N42, S20, S90
</details>

<details>
<summary>5.142 - Starting Longitude</summary>

**Definition/Description:** The Grid MORA table will contain records describing the MORA for each Latitude and Longitude block. Each record will contain thirty blocks and the "Starting Longitude" field defines the lower left corner for the first block of each record.

**Source/Content:** The "Starting Longitude" will be determined when the record is assembled.

**Used On:** Grid Mora records
**Length:** 4 characters
**Character Type:** Alpha/numeric
**Examples:** E000, W150, E090, W180
</details>

<details>
<summary>5.143 - MORA</summary>

**Definition/Description:** Minimum Off-route Altitude provides terrain and obstruction clearance within the section outlined by latitude and longitude blocks.

**Source/Content:** A MORA of 7,000 feet or less clears all known obstructions and terrain by 1,000 feet; a MORA greater than 7,000 feet clears all terrain by 2,000 feet. The field will contain values in hundreds of feet. For areas that are unsurveyed the field will contain the alpha characters "UNK".

**Used On:** Grid Mora record
**Length:** 3 characters
**Character Type:** Alpha/numeric
**Examples:** 071, 100, 123, UNK
</details>

<details>
<summary>5.144 - Center Fix (CENTER FIX)</summary>

**Definition/Description:** When used on Airport and Heliport MSA Records and specific terminal procedure records, the "Center Fix" field represents the MSA Center, that point (Navaid or Waypoint) on which the MSA is predicated. When used on Terminal Procedure Records incorporating an "RF" Path and Termination, the field represents the point (Terminal Waypoint) which defines the center of the arc flight path.

**Source/Content:** When used as "MSA Center," the field will contain the identification of the navigation facility or Enroute or Terminal Waypoint or Runway upon which the MSA coverage radius is predicated. Such content will be derived from official government sources. When used as "ARC Center," the field will contain the identification of the Terminal Waypoint used to define the arc. ARC Center waypoints can only appear in the Airport Terminal Waypoint or Heliport Terminal Waypoint Section/Subsections.

**Used On:** Airport and Heliport MSA Records, Airport and Heliport SID/STAR/Approach Records
**Length:** 5 characters max.
**Character Type:** Alpha/numeric
**Examples:** HOM, YXRNB, MM18, ARC02
</details>

<details>
<summary>5.145 - Radius Limit</summary>

**Definition/Description:** The altitude shown in the "Sector Altitude" field provides a 1000 foot obstacle clearance with a specified radius from the navigational facility/fix. The "Radius Limit" field allows the radius to be specified.

**Source/Content:** Radius limits will be derived from official government sources. Values will be shown in whole nautical miles.

**Used On:** Airport and Heliport MSA Records
**Length:** 2 characters
**Character Type:** Numeric
**Examples:** 25, 30
</details>

<details>
<summary>5.146 - Sector Bearing (SEC BRG)</summary>

**Definition/Description:** MSA is shown in a circle. When segments have different altitudes the dividing lines are shown as Sector Bearings toward the facility identified in the "Ident" field.

**Source/Content:** The "Sector Bearing" will be derived from official government sources. Each section requires three fields for definition. The first "Sector Bearing" shows the beginning bearing, in whole degrees, of the sector being defined. The second field "Sector Altitude" specifies the altitude for the sector and the third field "Sector Bearing" shows the end bearing, in whole degrees, of the sector being defined and is also the beginning bearing of the next sector to be defined. If the MSA is one sector or a complete circle, the first sector bearing field will contain the numeric "180".

**Used On:** Airport and Heliport MSA Records
**Length:** 3 characters
**Character Type:** Numeric
**Examples:** 060, 045, 090
</details>

<details>
<summary>5.147 - Sector Altitude (SEC ALT)</summary>

**Definition/Description:** The altitude shown in the "Sector Altitude" field provides a 1000 foot obstacle clearance within a specified radius from the navigational facility/fix.

**Source/Content:** Altitudes will be derived from official government sources. Values will be shown in hundreds of feet.

**Used On:** Airport and Heliport MSA Records
**Length:** 3 characters
**Character Type:** Numeric
**Examples:** 010, 025, 100
</details>

<details>
<summary>5.148 - Enroute Alternate Airport (EAA)</summary>

**Definition/Description:** The "Enroute Alternate Airport" field identifies the most suitable emergency airport along a Company Route.

**Source/Content:** This field is determined by the user airline and will contain the Airport ICAO Ident.

**Used On:** Company Route records
**Length:** 4 characters
**Character Type:** Alpha/numeric
**Examples:** KDEN, EGKK, EDFF
</details>

<details>
<summary>5.149 - Figure of Merit (MERIT)</summary>

**Definition/Description:** The "Figure of Merit" field is used to specify VHF NAVAID facility usable ranges beyond that specified in the Class field. It is also used to specify when a VHF NAVAID contained the database is not available for operational use, e.g. is out of service.

**Source/Content:** Actual Field Entry Values are not contained in official government source but rather are derived values based on usage, class, etc. These may be further adjusted by input from actual users. The content will be as defined in the table below.

| Field Entry | Description |
|---|---|
| 0 | Terminal Use (generally within 25NM) |
| 1 | Low Altitude Use (generally within 40NM) |
| 2 | High Altitude Use (generally within 130NM) |
| 3 | Extended High Altitude Use (generally beyond 130NM) |
| 9 | Out of Service |

**Used On:** VHF Navaid Records
**Length:** 1 character
**Character Type:** Numeric
</details>

<details>
<summary>5.150 - Frequency Protection Distance (FREQ PRD)</summary>

**Definition/Description:** The "Frequency Protection Distance" field provides an indication of the distance to the next nearest NAVAID on the same frequency.

**Source/Content:** The distance to the next NAVAID will be computer generated values. Values will be entered on NAVAID with DME or TACAN equipped facilities only and will indicate the distance, in nautical miles, to the next nearest DME or TACAN equipped facility. Maximum relevant value will be 600 nautical miles.

**Used On:** VHF Navaid records
**Length:** 3 characters
**Character Type:** Alpha/numeric
**Examples:** 030, 150, 600
</details>

<details>
<summary>5.151 - FIR/UIR Address (ADDRESS)</summary>

**Definition/Description:** The "FIR/UIR Address" field contains the four character communications address of the FIR/UIR to supplement the FIR/UIR Ident.

**Source/Content:** When addressing ATS messages to the ATS Center in charge of a FIR or UIR, a three-letter designator followed by a filler of "X" or by a letter representing a department or division within the organization addressed should be used. The three-letter designators are to be those defined in ICAO Document 8585, Designators for Aircraft Operating Agencies, Aeronautical Authorities 2 and Services. ICAO Document 7910, Location Indicators, Address of Centers in charge of FIR/UIR, states that when addressing ATS messages to the ATS Center in change of a FIR or a UIR, one of the following designators should be added to the location indicator to complete the addressee indicator:

If the message is related to an IFR Flight -- ZQZX
If the message is related to a VFR Flight -- ZFZX

To satisfy this requirement, unless otherwise stipulated by the user, the following address codes will be used:

ZOZX if related to an Oceanic FIR/UIR.
ZRZX if related to all other FIR/UIRs.

**Used On:** FIR/UIR and Enroute Communications records
**Length:** 4 characters
**Character Type:** Alpha
**Examples:** ZOZX, ZRZX
</details>

<details>
<summary>5.152 - Start/End Indicator (S/E IND)</summary>

**Definition/Description:** The "Start/End Indicator" field is used to indicate if the "Start/End Date" field is the effective start date, effective end date or the effective date for a change of the Primary record.

**Source/Content:**

| Field Entry | Description |
|---|---|
| C | Change Date |
| E | End Date |
| S | Start Date |

Note: If the Start/End Indicator field contains the alpha character "C" then the following continuation record is paired with it and the record will contain only the new values in the changed fields. All other fields will be blank.

**Used On:** Restrictive Airspace, VHF NAVAID, NDB NAVAID, Enroute, Terminal Waypoint, Airport Flight Planning Continuation and Heliport records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.153 - Start/End Date</summary>

**Definition/Description:** The "Start/End Date" when used on Continuation records specifies the effective Start/End date for a specific primary record when the effective date does not correspond with the AIRAC date. When used on Restriction records the Start and End dates specifies when the restrictions are in effect.

**Source/Content:** Effective dates will be derived from official government sources indicating the date/time in GMT of the effective date of the record or the effective times of the restriction. Default of the Start date is the current GMT date and default of the End date is forever.

**Used On:** Restrictive Airspace, VHF NAVAID, NDB NAVAID, Enroute, Terminal Waypoint, Airport Flight Planning Continuation and Heliport records
**Length:** 11 characters
**Character Type:** Alpha/numeric
**Examples:** 12JAN840000, 28SEP841200
</details>

<details>
<summary>5.154 - Restriction Identifier (REST IDENT)</summary>

**Definition/Description:** The "Restriction Identifier" is used to assign a unique identifier to a restriction record and to multiple restrictions records for a particular route or route segment.

**Source/Content:** Restriction Identifiers are assigned during the data file assembly. Initially the identifier will be assigned in sequence with the first restriction assigned the numeric value "001," the second "002," the third "003," etc. If a restriction record is removed, only that record is deleted and there will be no effect on the other identifiers for that airway; i.e., if record "002" is deleted, records "001" and "003" will retain their identifiers. If a new restriction is added, within a few cycles of the deletion of "002," it will use the next higher number even if there are gaps in the sequence of identifiers.

**Used On:** Airway Restriction and Airway Restriction Continuation records
**Length:** 3 characters
**Character Type:** Numeric
**Examples:** 001, 002, 003
</details>

<details>
<summary>5.157 - Airway Restriction Start/End Date (START/END DATE)</summary>

**Definition/Description:** The "Airway Restriction Start Date" field is used to indicate the earliest GMT date at which the restriction takes effect. The "Airway Restriction End Date" is used to indicate the latest GMT date at which the restriction is still in effect. This date information may be supplemented by "Time of Operation" information contained in an Airway Restriction Record, Type "AE" or "TC". When no "AE" or "TC" record exists for the Restriction Identifier, the Start time is 0000 GMT and the end time is 2359 GMT of the dates indicated.

**Source/Content:** When entered, start dates and end dates will be in the format DDMMMYY. If the YY portion is equal to blanks, the restriction is valid every year. When the start date is equal to blanks, the restriction is valid with immediate affect. When the end date is equal to blanks, the restriction is valid until further notice.

**Used On:** Enroute Airway Restriction records
**Length:** 7 characters
**Character Type:** Alpha/numeric
**Examples:** 15JAN92, 15 JAN (blank)
</details>

<details>
<summary>5.160 - Units of Altitude (UNIT IND)</summary>

**Definition/Description:** The "Units of Altitude" field is used to indicate the units of measurement for the values in the "Restriction Altitude" fields.

**Source/Content:** The actual values are derived from official government sources and expressed as one of the following codes.

| Field Entry | Description |
|---|---|
| F | Restriction Altitudes are expressed in hundreds of feet |
| K | Restriction Altitudes are expressed in metric Flight Levels |
| L | Restriction Altitudes are expressed in feet Flight Levels |
| M | Restriction Altitudes are expressed in tens of meters |

**Used On:** Airway Restriction records and Airway Restriction Continuation Records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.161 - Restriction Altitude (RSTR ALT)</summary>

**Definition/Description:** The "Restriction Altitude" fields are used to specify the altitude profile for a specific restriction.

**Source/Content:** Altitudes will be derived from official government sources and entered in hundreds of feet, tens of meters, standard or metric Flight Levels. The units used are determined through the "Units of Altitude" field. Altitudes are expressed in ascending order. All altitude fields after a "blank" altitude will also be blank.

**Used On:** Airway Restriction, Airway Restriction Continuation records
**Length:** 3 characters
**Character Type:** Numeric
**Examples:** 310 (standard FL310 or metric FL3199m or 31000 feet or 3100 meters); 090 (standard FL90 or metric FL900m or 9000 feet or 900 meters)
</details>

<details>
<summary>5.163 - Restriction Notes</summary>

**Definition/Description:** The "Restriction Notes" field may contain any restriction not otherwise covered by the altitude or time restriction.

**Source/Content:** Restriction notes will be derived from official government sources.

**Used On:** Airway Restriction continuation records
**Length:** 104 characters
**Character Type:** Alpha/Numeric
**Examples:** AVAILABLE FOR WESTBOUND DEPARTURES FROM GATWICK. EASTBOUND AND OVER-FLIGHTS BY ATC ONLY. REROUTING MUST BE EXPECTED MON-FRI 1800-2400 DUE TO MILITARY TRAFFIC.
</details>

<details>
<summary>5.164 - EU Indicator (EU IND)</summary>

**Definition/Description:** The "EU Indicator" field is used to identify those Enroute Airway records that have an Airway Restriction record without identifying the restriction.

**Source/Content:** The field will contain the alpha character "Y" when a restriction for the segment is contained in the restriction file or a blank when no restriction record exists.

**Used On:** Enroute Airways records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.166 - Channel</summary>

**Definition/Description:** The "Channel" field specifies the channel of the Azimuth, Elevation and Data transmissions for the MLS identified in the "MLS Identifier" field of the record.

**Source/Content:** Channels are derived from official government sources and range from 500 to 699.

**Used On:** MLS records
**Length:** 3 characters
**Character Type:** Numeric
</details>

<details>
<summary>5.167 - MLS Azimuth Bearing (MLS AZ BRG) MLS Back Azimuth Bearing (MLS BAZ BRG)</summary>

**Definition/Description:** The "MLS Azimuth Bearing" and the "MLS Back Azimuth Bearing" fields define the inbound magnetic final approach course of the MLS Azimuth and the MLS Back Azimuth facility described in the record.

**Source/Content:** MLS bearings derived from official government sources are entered into the field in degrees and tenths of degrees with the decimal point suppressed. For MLS Azimuth or Back Azimuth charted with true courses, the last character of this field will contain a "T" in place of tenths of a degree.

**Used On:** MLS and MLS Continuation records
**Length:** 4 characters
**Character Type:** Numeric
**Examples:** 0550, 0155, 015T
</details>

<details>
<summary>5.168 - Azimuth Proportional Angle Right/Left (AZ PRO RIGHT/LEFT) Back Azimuth Proportional Angle Right/Left (BAZ PRO RIGHT/LEFT)</summary>

**Definition/Description:** The "Azimuth Proportional Angle" fields define the limits of proportional guidance of the azimuth transmitter signal on the right and left side of the final approach course flight track. The BAZ is identical to the AZ and also provides guidance for missed approaches and departures. See figure under Section 5.172.

**Source/Content:** Azimuth Proportional angles will be derived from official government publications and entered in whole degrees.

**Used On:** MLS and MLS Continuation records
**Length:** 3 characters
**Character Type:** Numeric
**Examples:** 040, 025, 015
</details>

<details>
<summary>5.169 - Elevation Angle Span (EL ANGLE SPAN)</summary>

**Definition/Description:** The "Elevation Angle Span" field defines the scan of the elevation transmitter signal between the lower and upper limits.

**Source/Content:** Elevation angle span limits will be derived from official government publications and entered in degrees and tenths of degrees with the decimal point suppressed.

**Used On:** MLS records
**Length:** 3 characters
**Character Type:** Numeric
**Examples:** 300, 150
</details>

<details>
<summary>5.170 - Decision Height (DH)</summary>

**Definition/Description:** The "Decision Height" fields are used to specify a specific height in the precision approach at which a missed approach must be initiated if the required visual reference to continue the approach has not been established.

**Source/Content:** Decision Height information is obtained from official government publications and will be the ILS CAT I barometric related value. The field will contain a numeric value expressed in feet above touchdown, with a resolution of one foot. This value is also referred to as "Height Above Touchdown" (HAT), a figure which, when added to the touchdown zone, runway end or threshold elevation, will give the Decision Altitude in feet above mean sea level. These fields will be shown on the first record of the final approach only and may be blank if Minimum Descent Altitude fields are entered.

**Used On:** Airport and Heliport Approach Continuation Records.
**Length:** 4 characters
**Character Type:** Alpha/numeric
**Examples:** 0200
</details>

<details>
<summary>5.171 - Minimum Descent Height (MDH)</summary>

**Definition/Description:** The "Minimum Descent Height" fields specify the lowest height, expressed in feet, to which descent is authorized on final approach or during circle-to-land maneuvering in execution of a standard instrument approach procedure where no electric glide slope is provided.

**Source/Content:** Minimum Descent Height information is obtained from official government publications. The field will actually contain a figure expressed in feet above airport elevation, with a resolution of one foot. This value is also referred to as "Height Above Airport" (HAA), a figure which, when added to the airport elevation, will give the Minimum Descent Altitude in feet above mean sea level. These fields will be shown on the first record of the final approach only and may be blank if Decision Height fields are entered.

**Used On:** Airport and Heliport Approach Continuation Records.
**Length:** 4 characters
**Character Type:** Alpha/numeric
**Examples:** 0314, 0514
</details>

<details>
<summary>5.172 - Azimuth Coverage Sector Right/Left (AZ COV RIGHT/LEFT) Back Azimuth Coverage Sector Right/Left (BAZ COV RIGHT/LEFT)</summary>

**Definition/Description:** The "Azimuth Coverage Sector" fields define the limit of the azimuth transmitter signal on the right and left side of the final approach course flight track. The Back Azimuth Coverage Sector is identical to the Azimuth Coverage Sector and also provides guidance for missed approaches and departures.

**Source/Content:** Azimuth Coverage Sectors will be derived from official government publications and entered in whole degrees.

**Used On:** MLS and MLS Continuation records
**Length:** 3 characters
**Character Type:** Numeric
**Examples:** 040, 062, 110

COMMENTARY: The Azimuth Coverage Sector includes the Proportional Guidance Sector and the Clearance Guidance Sector as illustrated in below.
</details>

<details>
<summary>5.173 - Nominal Elevation Angle (NOM ELEV ANGLE)</summary>

**Definition/Description:** The "Nominal Elevation Angle" field defines the normal glide path angle for the MLS installation.

**Source/Content:** Glide Path angles from official government sources are entered into the field in tens of degrees, tenths of a degree and hundredths of a degree with the decimal point suppressed.

**Used On:** MLS records
**Length:** 4 characters
**Character Type:** Numeric
**Examples:** 1000, 0275
</details>

<details>
<summary>5.174 - Restrictive Airspace Link Continuation (LC)</summary>

**Definition/Description:** The "Restrictive Airspace Link Continuation" field is used to indicate cases where it is not possible to store all Enroute Airway to Restrictive Airspace Links in the Flight Planning Continuation Record defined in 4.6.3 (more than four area links required).

**Source/Content:** When an additional Continuation Record (as defined in 4.6.4) is required to provide further Enroute Airway to Restrictive Airspace Links, this field will contain the alpha character "Y" to indicate that status.

**Used On:** Enroute Airway Flight Planning Continuation records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.175 - Holding Speed (HOLD SPEED)</summary>

**Definition/Description:** The "Holding Speed" will be the maximum speed in a holding pattern.

**Source/Content:** The speed limit will be derived from official government sources. If the value is different from the limit given with ICAO rules, it will be shown in knots, else the field will be blank.

**Used On:** Holding Pattern record
**Length:** 3 characters
**Character Type:** Numeric
**Examples:** 250, 015
</details>

<details>
<summary>5.176 - Pad Dimensions</summary>

**Definition/Description:** The "Pad Dimensions" field defines the landing surface dimensions of the helicopter landing pad. The pad may be described as a rectangle or as a circle.

**Source/Content:** Pad dimensions will be derived from official government sources and entered into the field in feet with a resolution of one foot. When the pad is rectangular, the first three digits define one side of the landing pad and the last three digits the other side of the pad, e.g. "060120" indicates the pad is 60 feet by 120 feet. When the pad is circular, the first three digits define the diameter of the pad and the last three digits will be zeros, e.g., "080000" indicates a pad that is 80 feet in diameter.

**Used On:** Heliport record
**Length:** 6 characters
**Character Type:** Numeric
**Examples:** 060060, 100050, 040040
</details>

<details>
<summary>5.177 - Public/Military Indicator (PUB/MIL)</summary>

**Definition/Description:** Airports can be classified into three categories, airports open to the general public, military airports, and airport closed to the public. This field permits these airports to be categorized by their use.

**Source/Content:** Airport data is obtained from official government sources and their use is defined in these civil and or military publications. Airports that are considered joint use, both civil and military, will be shown as a civil airport.

| Field Content | Description |
|---|---|
| C | Airport/Heliport is open to the public (civil) |
| M | Airport/Heliport is military airport |
| P | Airport/Heliport is not open to the public (private) |

**Used On:** Airport and Heliport records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.178 - Time Zone</summary>

**Definition/Description:** The standard time zone system is based on the division of world into 24 zones, each of 15 degrees longitude. The "zero" time zone is entered at Greenwich meridian with longitudes 7 degrees, 30 minutes West and 7 degrees, 30 minutes east, and there is no difference in the standard time of this time zone and Greenwich Mean Time. Time zones are designated by letters of the alphabet by which the standard time of each zone differs from that at Greenwich.

**Source/Content:** Time zones will be derived from official Time Zone Charts of the World. The first character of the field indicates the time zone observed by the airport. Time zones are indicated by a letter of the alphabet according to the following table:

| Field Cont | Diff to Zulu time | Lat/Long Boundaries |
|---|---|---|
| Z | 0 | W007 30/E007 30 |
| A | -1 | E007 30/E022 30 |
| B | -2 | E022 30/E037 30 |
| C | -3 | E037 30/E052 30 |
| D | -4 | E052 30/E067 30 |
| E | -5 | E067 30/E082 30 |
| F | -6 | E082 30/E097 30 |
| G | -7 | E097 30/E112 30 |
| H | -8 | E112 30/E127 30 |
| I | -9 | E127 30/E142 30 |
| K | -10 | E142 30/E157 30 |
| L | -11 | E157 30/E172 30 |
| M | -12 | E172 30/180 00 |
| N | +1 | W007 30/W022 30 |
| O | +2 | W022 30/W037 30 |
| P | +3 | W037 30/W052 30 |
| Q | +4 | W052 30/W067 30 |
| R | +5 | W067 30/W082 30 |
| S | +6 | W082 30/W097 30 |
| T | +7 | W097 30/W112 30 |
| U | +8 | W112 30/W127 30 |
| V | +9 | W127 30/W142 30 |
| W | +10 | W142 30/W157 30 |
| X | +11 | W157 30/W172 30 |
| Y | +12 | W172 30/180 00 |

The second and third characters indicate, in minutes, that the time observed by the airport/heliport must be adjusted from the hour by the number of minutes indicated.

**Used On:** Airport and Heliport records
**Length:** 3 characters
**Character Type:** Alpha/numeric
**Examples:** India falls in the "E" (-5) and "F" (-6) time zones, however, the time zone observed in all of India is "E30" (-5 hours and 30 minutes). For any country falling into the "M" or "Y" time zone and observing a time equal to the next greater time zone, the adjustment of 1 hour will be indicated by "60" in the second and third positions.
</details>

<details>
<summary>5.179 - Daylight Time Indicator (DAY TIME)</summary>

**Definition/Description:** The "Daylight" Time Indicator" field is used to indicate if the airport observes Daylight or Summer time when such time changes are in effect for the country or state the airport resides in.

**Source/Content:** Countries and states that observe Daylight time will be obtained from official publications and the field will contain the alpha character "Y" if airport observes Daylight or Summer time. The field will contain the alpha character "N" if the airport does not observe Daylight time or if it is unknown.

**Used On:** Airport and Heliport records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.180 - Pad Identifier (PAD IDENT)</summary>

**Definition/Description:** The "PAD Identifier" field identifies the helipad described in the heliport records, helipad field, or that pad served by ILS/MLS described in the Airport and Heliport ILS/MLS records. There is a unique Heliport Record for each Helipad at a given location.

**Source/Content:** PAD Identifiers will be derived from official government publications when available. If not available from source, unique identifiers will be assigned by the data supplier.

**Used On:** Heliport, Airport and Heliport ILS and MLS Records
**Length:** Five characters
**Character Type:** Alpha/numeric
**Examples:** Source Supplied - PADA1, NWPAD, ALPHA, A1; Data Supplier - HELO1, HELO2, HELO3
</details>

<details>
<summary>5.187 - Distance Description (DIST DESC)</summary>

**Definition/Description:** The "Distance Description" field will designate whether a Communications frequency is to be used from the facility out to a specified distance or from a specified distance and beyond in the Airport Communications Record. In the VHF Navaid Limitation Continuation Record, the field is used to define whether the limitation applies from the navaid out to a specified distance or from a specified distance and beyond.

**Source/Content:** The field will contain the character "-" when the communications frequency or navaid limitation is "out to a specified distance." When the field content is "+", then the communications frequency is used or the navaid limitation applies "beyond" a specified distance. When the field is blank, no restrictions/limitations apply.

**Used On:** Airport Communications Records, VHF Navaid Limitation Continuation Records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.189 - Remote Site Name</summary>

**Definition/Description:** The "Remote Name" contains the name assigned to a Remote Communications Air/Ground and Remote Communications Outlet facilities. These remote facilities are unmanned air/ground communication stations with transmit and receive capability, used to extend the service range of ARTCC and FSS stations.

**Source/Content:** Remote Names are derived from official government publications. The field may be blank if names are not assigned.

**Used On:** Enroute Communications records.
**Length:** 25 characters
**Character Type:** Alpha/numeric
**Examples:** CHEYENNE, ABBEVILLE
</details>

<details>
<summary>5.190 - FIR/RDO Identifier (FIR/RDO)</summary>

**Definition/Description:** The "FIR/RDO Identifier" field for Enroute Center records identifies the Flight Information Region or Upper Information Region. For FSS records the field identifies the Flight Service Station.

**Source/Content:** Identifiers are obtained from official government publications. For FIR/UIR the field will contain the four character FIR or UIR ident. For other record type the field will contain a three or four character identifier.

**Used On:** Enroute Communications records.
**Length:** 4 characters
**Character Type:** Alpha/numeric
**Examples:** KZDN, DEN
</details>

<details>
<summary>5.195 - Time of Operation</summary>

**Definition/Description:** The "Time of Operation" field is used to indicate the times of operation of a Facility or Restriction.

**Source/Content:** The times of operation are derived from official government source. Each "Time of Operation" group contains the definition of a daily period of operations within a calendar week.

The first two positions identify days of the week, with Monday equal to 1 and Sunday equal to 7. A single day, for example, Monday, is depicted as "01". A consecutive series of days, for example Monday through Friday, is depicted as "15". Non-consecutive days require multiple Time of Operation entries. The remaining 8 characters define a starting time of four characters and an ending time of four characters. These times are in the format HHMM (H= hours, M= minutes) using a 24 hour time system. For example, 00012350 starts at one minute after midnight and ends at 10 minutes before midnight. 07152000 starts at 07:15 hours and ends at 20:00 hours.

Times of Operation can also be expressed in terms of Sunrise (SR) and Sunset (SS). When a "Time of Operation" is defined as starting at or ending at Sunrise, that time is specified as "000R". When a "Time of Operation" is defined as starting at or ending at Sunset, that time is specified as "000S". When a "Time of Operation" is defined as starting at or ending at a certain number of hours/minutes before or after Sunrise or Sunset, those times are specified as in the following examples:

030R for 30 minutes before Sunrise or R030 for 30 minutes after Sunrise.
100R for 1 hour before Sunrise or R100 for 1 hour after Sunrise.
030S for 30 minutes before Sunset or S030 for 30 minutes after Sunset.
100S for 1 hour before Sunset or S100 for 1 hour after Sunset.

Of the three digits associated with "R" or "S," the first is an expression of hours, the second and third an expression of minutes. 1 hour, 30 minutes would be 130, 2 hours, 15 minutes would be 215, etc.

When multiple definitions are required to fully define the "Time of Operation" for a given calendar week, these are coded as second and subsequent "Time of Operation" fields.

**Examples:** A restriction valid on Mondays, Wednesdays and Fridays only, 0700 to 1700, would require three "Time of Operation" entries, one for 01 (Monday), one for 03 (Wednesday), one for 05 (Friday) and would be expressed as 0107001700 0307001700 0507001700.

A continuous restriction, starting on Monday at 0700 and ending on Friday at 1700 would require three "Time of Operation" entries, one for Monday of 0107002359, one for Tuesday through Thursday of 2400002359 and one for Friday of 0500001700.

When the times to be defined go over midnight, the second four characters of time information are valid on the actual ending day. For example, a "Time of Operation" of Monday through Friday, 1700 to 0300 actually ends on Saturday and would be shown as 1617000300, not 1517000300.

**Used On:** Enroute Airway Restriction Primary and the following Continuation Records - Airport/Heliport/Enroute Communications, Restrictive Airspace, Preferred Route, Enroute Airway Restrictions and Controlled Airspace.
**Length:** 10 characters
**Character Type:** Alpha/Numeric
</details>

<details>
<summary>5.197 - Datum Code (DATUM)</summary>

**Definition/Description:** The "Datum Code" field defines the Local Horizontal Reference Datum to which a geographical position, expressed in latitude and longitude, is associated.

**Source/Content:** Local Horizontal Reference Datums will be derived from official government documentation. The "Datum Code" field will contain a three letter code corresponding to that government publication. A listing of valid three letter codes is contained in Attachment 2 to this Specification.

**Used On:** VHF Navaid, NDB Navaid, Terminal NDB, Enroute Waypoint, Airport, Fan Marker, Heliport and GLS Transmitter Records
**Length:** 3 characters
**Character Type:** Alpha
**Examples:** AGD, NAS, WGA
</details>

<details>
<summary>5.199 - Signal Emission (SIG EM)</summary>

**Definition/Description:** High Frequency (HF) signals used in aeronautical communications can be the complete signal or a portion of the signal, called a sideband. The "Signal Emission" field will designate for each HF Frequency what emission is used.

**Source/Content:** This field contains the following information:

| Field Content | Description |
|---|---|
| 3 | Double Sideband (A3) |
| A | Single sideband, reduced carrier (A3A) |
| B | Two Independent sidebands (A3B) |
| H | Single sideband, full carrier (A3H) |
| J | Single sideband, suppressed carrier (A3J) |
| L | Lower (single) sideband, carrier unknown |
| U | Upper (single) sideband, carrier unknown |

Note: The field is blank on records with frequencies that are not HF, see Section 5.104.

**Used On:** Enroute, Airport and Heliport Communications Records
**Length:** 1 character
**Character Type:** Alpha/Numeric
</details>

<details>
<summary>5.200 - Remote Facility (REM FAC)</summary>

**Definition/Description:** The "Remote Facility" field is used to define the Navaid that a Remote Communications Outlet (RCO) will be transmitting through.

**Source/Content:** Navaids used as RCOs will be derived from official government publications and the field will contain the official 2,3 or 4 character Navaid Identifier.

**Used On:** Enroute, Airport and Heliport Communications Records.
**Length:** 4 characters
**Character Type:** Alpha/Numeric
</details>

<details>
<summary>5.201 - Restriction Record Type (REST TYPE)</summary>

**Definition/Description:** The "Restriction Record Type" field is used to define what type of a restriction is contained in the Enroute Airway Restriction Record in question.

**Source/Content:** The content of this field should be selected from the following listing of possible codes:

AE = Altitude Exclusion. The record contains altitudes, normally available, that are excluded from use for the Enroute Airway Segment. May be further restricted by "Time of Operation" information.

TC = Cruising Table Replacement. The record contains only a reference to a Cruising Table Identifier. That Cruise Table will be in force, replacing the Cruise Table Identifier in the Enroute Airway segment records defined in the "Start Fix/End Fix" fields.

SC = Seasonal Restriction. Record is used to close an Airway or portion of an Airway on a seasonal basis.

NR = Note Restrictions. The record contains restrictions that do not fit the pattern of "formatted" information allowed by other "Restriction Record Types".

**Used On:** Enroute Airway Restriction Records
**Length:** 2 characters
**Character Type:** Alpha
</details>

<details>
<summary>5.202 - Exclusion Indicator (EXC IND)</summary>

**Definition/Description:** The "Exclusion Indicator" field is an indication of how the altitudes contained in the Cruising Table record referenced by the Airway segment(s) are restricted. This is an "all altitude" restriction, further defined by direction of flight. These codes will not be used when certain altitudes remain available in a direction of flight.

**Source/Content:** The content of the field will be one of the codes from the following listing:

"A" = All altitudes in both directions of flight are restricted. This effectively closes the airway in both direction of flight.

"B" = All altitudes in the opposite direction in which the Enroute Airway is coded are restricted. This effectively closes the airway in one direction of flight i.e., the opposite direction from that in which the airway is coded.

"F" = All altitudes in the direction in which the Enroute Airway is coded are restricted. This effectively closes the airway in one direction of flight i.e., the direction in which the airway is coded.

(blank) = The restriction is not an "all altitude" restriction.

**Used On:** Enroute Airway Restriction Records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.203 - Block Indicator (BLOCK IND)</summary>

**Definition/Description:** The "Block Indicator" field is used to specify that the altitudes that follow in the restriction record are either "block" of altitudes that are restricted (not available for flight) or are individual altitudes that are restricted.

**Source/Content:** The field will either be set to "B" indicating an altitude block or "I" indicating individual altitudes. One or the other or both codes will appear in restriction records that are not "Exclusive" restrictions (see Section 5.201).

**Used On:** Enroute Airway Restriction Records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.204 - ARC Radius (ARC RAD)</summary>

**Definition/Description:** The "ARC Radius" field is used to define the radius of a precision arc in the "Constant Radius To A Fix" Path and Termination, the "RF" Leg.

**Source/Content:** The content of the field will be derived from official source publications. It will be expressed in nautical miles, tenths, hundredths and thousandths of a nautical mile, with the decimal point suppressed. A conversion to feet of the resolution in nautical miles is equal to an accuracy of 6 feet.

**Used On:** SID, STAR and Approach Records
**Length:** 6 characters
**Character Type:** Numeric
**Examples:** 246868, 460820, 691231
</details>

<details>
<summary>5.205 - Navaid Limitation Code (NLC)</summary>

**Definition/Description:** The "Navaid Limitation Codes" field is used to define the type of limitation to be expected with a VHF Navaid.

**Source/Content:** The type of limitation will be derived from official government publications and entered using one of the codes defined in the table.

| Content | Limitation Description |
|---|---|
| C | Coverage, the limitations are expressed as maximum reception reliability |
| F | Fluctuations, radial(s) are affected by course fluctuations. |
| G | Roughness, signal roughness experienced in the sector(s) defined. |
| N | Unreliable in the sector(s), at the altitude(s), at the distance(s) defined. |
| R | Restricted in the sector(s), at the altitude(s), at the distance(s) defined. |
| T | Unusable in the sector(s), at the altitude(s), at the distance(s) defined. |
| U | Out of Tolerance in the sector(s), at the altitude(s), at the distance(s) defined. |

**Used On:** VHF Navaid Limitation Continuation Records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.206 - Component Affected Indicator (COMP AFFTD IND)</summary>

**Definition/Description:** The VHF Navaid File contains navaids that have one or two components - azimuth and/or distance. Published limitations may apply to one or both of the components. The "Component Affected Indicator" defines which component(s) are affected by the limitation.

**Source/Content:** The field content will be entered as indicated in the table based on official government publications. When different limitations apply to different components or components pairs, this will result in multiple Component Affected Indicators for a single navaid to cover the complete limitation. In these cases, the Sequence Number (Section 5.12) will start again with one (01) with each new Component Affected Indicator.

| Content | Component Description |
|---|---|
| A | TACAN or VORTAC, TACAN azimuth component only affected. |
| B | VORDME, or VORTAC, both azimuth and distance component affected. |
| D | VORDME or DME, distance component only affected. |
| M | VORTAC or TACAN, TACAN azimuth and distance component affected. |
| T | TACAN or VORTAC, distance component affected. |
| V | VOR, VORDME or VORDME, VOR azimuth component affected. |
| Z | VORDME, VORTAC or TACAN, VOR and TACAN azimuth and distance component affected. |

**Used On:** VHF Navaid Limitation Continuation Records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.207 - Sector From/Sector To (SECTR)</summary>

**Definition/Description:** The "Sector From/Sector To" field defines sectorization applicable to the range limited sectors of VOR/DME, VORTAC or TACAN facilities, using the sector letters from the table. Each sector is described by two characters and is to be interpreted as "from" the first character, clockwise "to" the second character.

**Source/Content:** Field content is derived through interpretation of official government publication information which may be in a variety of formats.

| Sector Character | From (degrees true) | To (degrees true) |
|---|---|---|
| A | 000 | 015 |
| B | 015 | 030 |
| C | 030 | 045 |
| D | 045 | 060 |
| E | 060 | 075 |
| F | 075 | 090 |
| G | 090 | 105 |
| H | 105 | 120 |
| I | 120 | 135 |
| J | 135 | 150 |
| K | 150 | 165 |
| L | 165 | 180 |
| M | 180 | 195 |
| N | 195 | 210 |
| O | 210 | 225 |
| P | 225 | 240 |
| Q | 240 | 255 |
| R | 255 | 270 |
| S | 270 | 285 |
| T | 285 | 300 |
| U | 300 | 315 |
| V | 315 | 330 |
| W | 330 | 345 |
| X | 345 | 000 |

**Used On:** VHF Navaid Limitation Continuation Records
**Length:** 2 characters
**Character Type:** Alpha
**Examples:** AB, TA, LW
</details>

<details>
<summary>5.208 - Distance Limitation (DIST LIMIT)</summary>

**Definition/Description:** The "Distance Limitation" field is used to define the distance(s) from the navaid at which the limitation applies.

**Source/Content:** "Distance Limitations" are derived from official government publications. The field will contain one or two distances expressed in nautical miles from the facility. Used together with the "Distance Description" field, the distances can be provided as indicated in the table of examples. The field will be blank if there are no distances associated with the limitation.

| Distance Description | Distance Limit - First Three Digits | Distance Limit - Second Three Digits | Description of Content |
|---|---|---|---|
| _ (blank) | 040 | 000 | Limitation valid out to 40NM from the facility. |
| + | 040 | 000 | Limitation valid beyond 40NM from the facility. |
| B | 100 | 040 | Limitation valid between 40NM and 100NM. |
| Blank | 040 | 000 | Limitation valid at 40NM from the facility. |

**Used On:** VHF Navaid Limitation Continuation Records
**Length:** 6 characters
**Character Type:** Alpha/Numeric
</details>

<details>
<summary>5.209 - Altitude Limitation (ALT LIMIT)</summary>

**Definition/Description:** The "Altitude Limitation" field is used to define the altitude(s) at which the limitation applies.

**Source/Content:** "Altitude Limitations" are derived from official government publications. The field will contain one to two altitudes, expressed in hundreds of feet MSL. Used together with the "Altitude Description" field, the altitudes can be provided as indicated in the table of examples. The field will be blank if there are no altitudes associated with the limitation.

| Altitude Description | Altitude Limit - First Three Digits | Altitude Limit - Second Three Digits | Description of Content |
|---|---|---|---|
| - | 040 | 000 | Limitation valid at or below 4000'/FL040. |
| + | 040 | 000 | Limitation valid at or above 4000'/FL040. |
| B | 100 | 040 | Limitation valid from 4000'/FL040 to 10000'/FL100. |
| blank | 040 | 000 | Limitation valid at 4000'/FL040. |

**Used On:** VHF Navaid Limitation Continuation Records
**Length:** 6 characters
**Character Type:** Alpha/Numeric
</details>

<details>
<summary>5.210 - Sequence End Indicator (SEQ END)</summary>

**Definition/Description:** The "Sequence End Indicator" field is used to define the end of a set of sequences defining a given limitation to a given VHF Navaid Component or Component pair.

**Source/Content:** "Limitations" are derived from official government publications. The field will contain the character "E" in that sequence which is the end of a given limitation.

**Used On:** VHF Navaid Limitation Continuation Records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.217 - Controlled Airspace Indicator (CTLD ARSP IND)</summary>

**Definition/Description:** The "Controlled Airspace Indicator" field is used to indicate if an airport is associated with controlled airspace of a terminal type such as a Terminal Control Area (TMA or TCA) Radar Area or Class B or C Airspace within the USA.

**Source/Content:** Airports lying within or below terminal controlled airspace will be determined through the use of official government publications describing the lateral limits of such airspace. The Controlled Airspace Airport/ICAO fields identify the airport for which terminal controlled airspace has been included in the Controlled Airspace Section of the file. The Controlled Airspace Indicator field will contain one of the codes from the table below. If an airport is not associated with any terminal controlled airspace of the types in this table, the Controlled Airspace Indicator field will be blank. The Controlled Airspace Airport/ICAO may be identical to or different than the record airport. Although Control Zones (CTR) are provided as Controlled Airspace, no reference to them is made in this manner in the Airport Flight Planning Continuation Record.

| Field Content | Description |
|---|---|
| A | The Airport is within or below the lateral limits of Class C Airspace. |
| C | The Airport is within or below the lateral limits of a CTA. |
| M | The Airport is within or below the lateral limits of a TMA or TCA. |
| R | The Airport is within or below the lateral limits Radar Zone. |
| T | The Airport is within or below the lateral limits of Class B Airspace. |

**Used On:** Airport Flight Planning Continuation Records
**Length:** 1 character
**Character Type:** Alpha
</details>

<details>
<summary>5.222 - GPS/FMS Indicator (GPS/FMS IND)</summary>

**Definition/Description:** The "GPS/FMS Indicator" field provides an indication of whether or not the responsible government agency has authorized the overlay of a conventional, ground-based aid approach procedure with the use of a GPS sensor or if the procedure may be flown with FMS as the primary navigation equipment.

**Source/Content:** The Indicator will be selected from the table below.

| Field Content | Indicator Definition |
|---|---|
| 0 | Procedure Not Authorized for GPS or FMS Overlay |
| 1 | Procedure Authorized for GPS Overlay, primary Navaids operating and monitored |
| 2 | Procedure Authorized for GPS Overlay, primary Navaids installed, not monitored |
| 3 | Procedure Authorized for GPS Overlay, Procedure Title includes "GPS" |
| 4 | Procedure Authorized for FMS Overlay |
| 5 | Procedure Authorized for FMS and GPS Overlay |
| U | Procedure Overlay Authorization unspecified (See Note 1) |

**Used On:** Airport and Heliport Approach Procedure Records
**Length:** One character
**Character Type:** Alpha/Numeric
</details>

<details>
<summary>5.223 - Operations Type (OPS TYPE)</summary>

**Definition/Description:** The "Operations Type" field contains information on parameters such as "approach procedure," or "advanced operations" or others still to be defined. Advanced operations can be straight-in approaches followed by a precision missed approach, a precision curved approach or departure procedure, etc.

**Source/Content:** A code derived from government source documentation.

**Used On:** Path Point Records
**Length:** 2 Characters
**Character Type:** Alpha/numeric
**Examples:** Content TBD, Default Blank
</details>

<details>
<summary>5.224 - Approach Indicator (APP IND)</summary>

**Definition/Description:** The "Approach Indicator" field is a single alphanumeric character used to differentiate between multiple RNAV - GPS/GLS final approach paths to the same runway. The first such procedure is labeled "0," additional approaches are incrementally numbered.

**Source/Content:** A code of "0" through "9" or "A" through "Z," excluding "I" and "O," based on government source documentation.

Note: This single character is consistent with the "Multiple Approach Indicator" included as the fifth character of an Approach Procedure Identifier.

**Used On:** Path Point Records
**Length:** One Character
**Character Type:** Alpha/Numeric
</details>

<details>
<summary>5.225 - Ellipsoidal Height</summary>

**Definition/Description:** The "Ellipsoidal Height" field is the height of a surveyed point in reference to the WGS-84 ellipsoid.

**Source/Content:** The Ellipsoidal Height will be derived from official government source and entered with a resolution of one foot or one meter. When the height is below the ellipsoid, the first position will carry a minus (-) sign, otherwise this position will be a plus (+) sign.

**Used On:** Path Point Records
**Length:** 6 Characters
**Character Type:** Alpha/numeric
**Examples:** +00356, +00051, +015, -00022, -01566
</details>

<details>
<summary>5.226 - Glide Path Angle (GPA)</summary>

**Definition/Description:** The "Glide Path Angle" field is an angle, expressed in degrees, tenths and hundredths of degrees, measured at the Flight Path Control Point (FPCP) of a RNAV - GPS/GLS Approach Procedure that establishes the intended descent gradient for the final approach flight path.

**Source/Content:** The values will be derived from official government source.

**Used On:** Path Point Records
**Length:** 4 Characters
**Character Type:** Numeric
**Examples:** 0275 (is equal to 2.75°), 1015 (is equal to 10.15°), 0300 (is equal to 3.00°)
</details>

<details>
<summary>5.227 - Orthometric Height (ORTH HGT)</summary>

**Definition/Description:** The "Orthometric Height" field is the height of a surveyed point in reference to Mean Sea Level (MSL).

**Source/Content:** The Orthometric Height will be derived from official government source and entered with a resolution of one foot or one meter. When the height is below MSL, the first position will carry a minus (-) sign, otherwise this position will be a plus (+) sign.

**Used On:** Path Point Records
**Length:** 6 Characters
**Character Type:** Alpha/numeric
**Examples:** +00356, +00051, +01566, -00022, -01566
</details>

<details>
<summary>5.228 - Unit of Height (UNIT)</summary>

**Definition/Description:** The "Unit of Height" field is used in Path Point Records for ellipsoidal and orthometric heights. These heights may be provided in government publications in either feet or meters. As these height fields are included in the "CRC Wrap," meter values cannot be converted to feet as they would be in other places in ARINC 424 File preparation.

**Source/Content:** The field will contain the character "F" if the height values were provided in source documentation in feet or the character "M" if those heights were provided in meters.

**Used On:** Path Point Records
**Length:** One character
**Character Type:** Alpha
</details>

<details>
<summary>5.229 - Path Point Data CRC (CRC)</summary>

**Definition/Description:** The "Path Point Data CRC" field is an eight (8) character hexadecimal representation of the 32-bit CRC value provided by the source for the information contained in the aeronautical data fields being monitored for integrity. The value is calculated by a specific mathematical algorithm, which is both machine and man processible.

**Source/Content:** The CRC calculation information is available as Chapter Six of this Specification.

**Used On:** Path Point Records
**Length:** Eight Characters
**Character Type:** Alpha/numeric
**Examples:** 243BC649, A6934B72
</details>

<details>
<summary>5.230 - Procedure Type (PROC TYPE)</summary>

**Definition/Description:** The "Procedure Type" field used on Flight Planning Arrival/Departure Data Record is a single character code indication the type of procedure in the record, such as Arrival, Standard Instrument Arrival Route, Approach.

**Source/Content:** The Procedure Type code must be one of the following codes:

| Procedure Type Code | Procedure Type Description |
|---|---|
| A | Arrival Procedure, Available in Database |
| B | Arrival Procedure, Not Available in Database |
| C | Departure Procedure, Available in Database |
| D | Departure Procedure, Not Available in Database |
| E | Standard Terminal Arrival Route (STAR), Available in Database |
| F | Standard Terminal Arrival Route (STAR), Not Available in Database |
| G | Standard Instrument Departure (SID), Available in Database |
| H | Standard Instrument Departure (SID), Not Available in Database |
| I | Vector SID, Available in Database |
| J | Vector SID, Not Available in Database |
| K | Approach Procedure, Available in Database |
| L | Approach Procedure, Not Available in Database |

**Used On:** Flight Planning Arrival/Departure Data records
**Length:** One character
**Character Type:** Alpha
</details>

<details>
<summary>5.231 - Along Track Distance (ATD)</summary>

**Definition/Description:** The "Along Track Distance" field used on Flight Planning Arrival/Departure Data Records is the total distance for a given transition, from the initial fix to the ending fix in the transition. A single occurrence of a Flight Planning Arrival/Departure Data record can contain up to three Along Track Distance fields, one for each of the transition types that can make up a single terminal route in the Primary Record and up to four possible intermediate fix points in each Continuation Record. Collectively, the values equal the along track distance from the first fix in the first transition to the last fix in the last transition.

**Source/Content:** The along track distances will be calculated by data suppliers using coded terminal procedures or uncoded terminal procedures derived from official government source and expressed in nautical miles with a 1NM resolution.

**Used On:** Flight Planning Arrival/Departure Data records
**Length:** 3 characters
**Character Type:** Numeric
</details>

<details>
<summary>5.232 - Number of Engines Restriction (NOE)</summary>

**Definition/Description:** The "Number of Engines Restriction" field used on Flight Planning Arrival/Departure Data Records is derived from government source and is included whenever a given procedure, normally departure, is restricted to, or designed for, aircraft with a specific number of engines.

**Source/Content:** The number of engines will be taken from official government source. The field will contain the character Y for each engine configuration position, 1, 2, 3 and 4, for which the procedure is authorized. Non-authorized configuration positions will contain the character N.

**Used On:** Flight Planning Arrival/Departure Data records
**Length:** 4 characters
**Character Type:** Alpha
**Examples:** YYYY (1, 2 3 or 4 Engine aircraft may use procedure); NNYY (3 and 4 Engine aircraft may use procedure)
</details>

<details>
<summary>5.233 - Turboprop/Jet Indicator (TURBO)</summary>

**Definition/Description:** The "Turboprop/Jet Indicator" field used on Flight Planning Arrival/Departure Data Records is derived from government source and is included whenever a given procedure, normally departure, is restricted to, or designed for, aircraft with a specific kind of engines.

**Source/Content:** The indication of Turboprop, Jet or Both on the use restriction of given procedure will be taken from official government source. The field will indicate the use restriction with a character from the table below.

| Field Content | Aircraft or Aircraft Group |
|---|---|
| A | All Aircraft |
| B | Jets and Turbo Props |
| C | All Aircraft, Cruise speed 250 kts or less |
| D | Non-jet and Turbo Prop |
| E | Multi-Engine Props Only |
| J | Jets |
| N | Non-Jet, Non-Turbo Prop |
| P | Turbo Props |

**Used On:** Flight Planning Arrival/Departure Data Records
**Length:** One character
**Character Type:** Alpha
</details>

<details>
<summary>5.234 - RNAV Flag (RNAV)</summary>

**Definition/Description:** The "RNAV Flag" field used on Flight Planning Arrival/Departure Data Records is derived from government source and is included whenever a given procedure included in the record is restricted to, or designed for, aircraft capable of flying RNAV Procedures.

**Source/Content:** The indication of RNAV, Yes or No, on a given procedure will be taken from official government source. The field will indicate Y for "Yes," the procedure is an RNAV procedure or N for "No," the procedure is not RNAV.

**Used On:** Flight Planning Arrival/Departure Data records
**Length:** One character
**Character Type:** Alpha
</details>

<details>
<summary>5.235 - ATC Weight Category (ATC WC)</summary>

**Definition/Description:** The "ATC Weight Category" field used on Flight Planning Arrival/Departure Data Records is derived from government source and is included whenever a given procedure included in the record is restricted to, or designed for, a specific aircraft weight grouping.

**Source/Content:** The indication of Heavy, Medium or Light aircraft on a given procedure will be taken from official government source. The field will be derived from that source to indicate:

H for Heavy, all aircraft types of 136,000kg (300000LB) or more.
M for Medium, aircraft types less than 136,000kg (300,000LB) and more than 7,000kg (155,000LB).
L for Light, aircraft types of 7,000kg (155,000LB) or less.

**Used On:** Flight Planning Arrival/Departure Data records
**Length:** One character
**Character Type:** Alpha
</details>

<details>
<summary>5.236 - ATC Identifier (ATC ID)</summary>

**Definition/Description:** The "ATC Identifier" field used on Flight Planning Arrival/Departure Data Records is the indication of the officially published procedure designation which is required for Flight Planning.

**Source/Content:** The ATC Identifier will be derived from official government source. This seven character field is required in addition to the six character identifier, the former is used in Flight Planning, the latter in accessing the database.

**Used On:** Flight Planning Arrival/Departure Data records
**Length:** 7 characters
**Character Type:** Alpha/numeric
</details>

<details>
<summary>5.237 - Procedure Description (PROC DESC)</summary>

**Definition/Description:** The "Procedure Description" field used on Flight Planning Arrival/Departure Data Records is the textual representation of the procedure name.

**Source/Content:** The Procedure Description will be derived from official government source. It will assist in matching flight plan content to charted procedures.

**Used On:** Flight Planning Arrival/Departure Data records
**Length:** 15 characters
**Character Type:** Alpha/numeric
</details>

<details>
<summary>5.238 - Leg Type Code (LTC)</summary>

**Definition/Description:** The "Leg Type Code" field used on Flight Planning Arrival/Departure Data Records is a simplification of the Path Terminator concept. It will provide the information on the path between intermediate waypoints as straight or curved and provide an indication of the change in direction of flight, expressed as left or right, at an intermediate waypoint.

**Source/Content:** The Leg Type Code will be derived from official government source. In this two character field, the first position will indicate with the character S, straight line point to point and with the character C, curved line flight track. The second position will be used as a turn indication, L for Left and R for Right when there is a turn requirement at an intermediate waypoint.

**Used On:** Flight Planning Arrival/Departure Data records
**Length:** 2 characters
**Character Type:** Alpha
</details>

<details>
<summary>5.239 - Reporting Code (RPT)</summary>

**Definition/Description:** The "Reporting Code" field used on Flight Planning Arrival/Departure Data Records is a simplification of the Waypoint Description concept. It will provide the information on intermediate waypoints as either Position Report Required (Compulsory Report) or Position Report Not Required (On-Request Report).

**Source/Content:** The Reporting Code will be derived from official government source. In this single character field, the code "C" will indicate Position Report Required and the code "X" Position Report Not Required.

**Used On:** Flight Planning Arrival/Departure Data records
**Length:** One character
**Character Type:** Alpha
</details>

<details>
<summary>5.240 - Altitude (ALT)</summary>

**Definition/Description:** The "Altitude" field used on Flight Planning Arrival/Departure Data Records is a simplification of the altitude concept used in the full procedure records. It will provide an altitude indication in hundreds of feet, no AGL, MSL, FL etc indication provided.

**Source/Content:** The Altitude will be derived from official government source and reduced to this flight planning resolution requirement.

**Used On:** Flight Planning Arrival/Departure Data records
**Length:** 3 character
**Character Type:** Numeric
**Examples:** FL100 = 100; 10000 feet = 100; 03500 feet = 035
</details>

<details>
<summary>5.241 - Fix Related Transition Code (FRT Code)</summary>

**Definition/Description:** The "Fix Related Transition Code" is used on Flight Planning Arrival/Departure Data Continuation Records containing Intermediate Fix information and provides an indication, through use of the standard coding practices of separating the procedure into transitions, as to where in the procedure the intermediate fix is located.

**Source/Content:**

| Intermediate Fix is Located in Transition | Field Content |
|---|---|
| Fix Located in SID Runway Transition | 1 |
| Fix Located in SID Common Portion | 2 |
| Fix Located in SID Enroute Transition | 3 |
| Fix Located in STAR Enroute Transition | 4 |
| Fix Located in STAR Common Portion | 5 |
| Fix Located in STAR Runway Transition | 6 |

**Used On:** Flight Planning Arrival/Departure Data records
**Length:** One character
**Character Type:** Numeric
</details>

<details>
<summary>5.242 - Procedure Category (PROC CAT)</summary>

**Definition/Description:** The Airport and Heliport SID/STAR/Approach Procedure Route Type supports the "All Sensor RNAV" Approach procedure. This kind of approach will have multiple sets of weather minimums (DH and NDA) associated with it. This field identifies the Procedure Categories for which these minimums apply.

**Source Content:** The field will contain a coded category from the following table:

| Content | Procedure Category |
|---|---|
| LAAS | Local Area Differential Augmentation System |
| WAAS | Wide Area Differential Augmentation System |
| FMS | Flight Management System |
| GPS | Global Positioning System, no Augmentation |
| VDME | VORDME, VORTAC |
| CIRC | Circle-To-Land |

**Used On:** Airport and Heliport SID/STAR/Approach Procedure Continuation Records
**Length:** 4 characters
**Character Type:** Alpha
</details>

<details>
<summary>5.243 - GLS Station Identifier</summary>

**Definition/Description:** The "GLS Identifier" field defines the identification code for retrieval of such a transmitter from a database. This is not a transmitted identifier.

**Source/Content:** The content of this field will be the Airport or Heliport ICAO Location Identifier Code at which the transmitter is installed.

**Used On:** GLS Records
**Length:** 4 characters max
**Character Type:** Alpha/numeric
</details>

<details>
<summary>5.244 - GLS Channel</summary>

**Definition/Description:** The "GLS Channel" field identifies the channel that will be decoded to identify the frequency of the differential GLS ground station and the approach information that will be sent by the differential GLS ground station.

**Source/Content:** The values for this field will be derived from official government sources and entered a five character channel identification code. The range is 20000 to 99999.

**Used On:** GLS Records
**Length:** 5 character
**Character Type:** Numeric
**Examples:** 20010, 56234
</details>

<details>
<summary>5.245 - Service Volume Radius</summary>

**Description/Definition:** The service volume radius identifies the radius of the service volume around the transmitter in Nautical miles.

**Source/Content:** The value for this field will be derived from official government sources. If no source is provided, the default value will be blanked.

**Used On:** GLS Record
**Length:** 2 characters
**Character Type Numeric**
**Examples:** 05, 19
</details>

<details>
<summary>5.246 - TDMA Slots</summary>

**Definition/Description:** The TDMA identifies the time slot(s) in which the ground station transmits the related approach. The high precision time source available through GPS permits utilization of Time division multiplexing or TDMA (Time Division Multiple Access), allowing multiple ground stations to share a common frequency by dividing it into eight time slots. An individual station may broadcast in one or more of eight slots.

**Source/Content:** The value for this field will be derived from official government sources. The range is 01 to FF. If no source is provided, the default value will be blank.

**Used On:** GLS Record
**Length:** 2 characters
**Character Type:** Alpha/numeric
**Examples A2, 01, FF**
</details>

<details>
<summary>5.247 - Station Type</summary>

**Description/Definition:** The station type identifies the type of the differential ground station. The first character will be L for LAAS/GLS ground station, C for SCAT-1 station. The second and third character will be blank for the moment. They will indicate the interoperability standard to which the station conforms.

**Source/Content:** The value for this field will be derived from official government sources. If LAAS/GLS or SCAT-1 is not specified in source, the default value will be blank.

**Used on:** GLS record
**Length:** 3 characters
**Character type:** Alpha/Numeric
**Examples:** L, C
</details>

<details>
<summary>5.248 - Station Elevation WGS84</summary>

**Description/Definition:** This field identifies the WGS84 elevation of the GLS ground station described in the record.

**Source/Content:** The value for this field will be derived from official government sources or entered into this field in feet with respect to the WGS84 ellipsoid. When elevation is below the WGS 84 ellipsoid, the first column of the field contains a minus (-) sign.

**Used on:** GLS record
**Length:** 5 characters
**Character type:** Alpha/Numeric
**Examples:** 00530, -0140
</details>

<details>
<summary>5.249 - Longest Runway Surface Code (LRSC)</summary>

**Definition/Description:** The "Longest Runway Surface Code" field is used to define whether or not there is a hard surface runway at the airport, the length of which is indicated in the Longest Runway field.

**Source/Content:** The content will be selected from the table below.

| Field Content | Description |
|---|---|
| H | Hard Surface, for example, asphalt or concrete |
| S | Soft Surface, for example, gravel, grass or soil |
| W | Water Runway |
| U | Undefined, surface material not provided in source |

**Used On:** Airport Records
**Length:** One character
**Character Type:** Alpha
</details>

<details>
<summary>5.250 - Alternate Record Type (ART)</summary>

**Definition/Description:** The "Alternate Record Type" field identifiers the record as being applicable to the departure airport (take-off alternate), destination airport (arrival alternate) or a fix along the route (enroute alternate).

**Source/Content:** The "Alternate Record Type" will be selected from the following table:

| Content | Description |
|---|---|
| AA | The Airport identifier in Columns 7 through 11 of the Primary Record are the identifier of the Arrival Airport. |
| DA | The Airport identifier in Columns 7 through 11 of the Primary Record are the identifier of the Departure Airport. |
| EA | The end fix of a Company Route is identified in Columns 7 through 15 of the Primary Record. |

**Used On:** Alternate Records
**Length:** 2 characters
**Character Type:** Alpha
</details>

<details>
<summary>5.251 - Distance To Alternate (DTA)</summary>

**Definition/Description:** The "Distance To Alternate" field defines either the direct (geodesic) distance from the Destination Airport or Fix to the Alternate Airport or the along track distance of an alternate Company Route.

**Source/Content:** When the Alternate Type field carries the character "A," the Distance to Alternate field carries the straight line (geodesic) distance in nautical miles between the Destination Airport or Fix and the Alternate Airport as listed in the Alternate Identifier fields. When the Alternate Type field carries the character "C," the Distance to Alternate field carries the cumulative along track distance for the Alternate Company Route as listed in the Alternate Identifier fields.

**Used On:** Alternate Records
**Length:** Three characters max.
**Character Type:** Numeric
</details>

<details>
<summary>5.252 - Alternate Type (ALT TYPE)</summary>

**Definition/Description:** The "Alternate Type" field is an information processing indicator. The Alternate Destination can be defined as an airport or an airport and route to an airport. This field defines that an alternate airport or, an company route is defined in the Alternate Identifier fields.

**Source/Content:** The field will contain either the character "A" when an Airport is provided or the character "C" when a Company Route is provided.

**Used On:** Alternate Records
**Length:** One character
**Character Type:** Alpha
</details>

<details>
<summary>5.253 - Primary and Additional Alternate Identifier (ALT IDENT)</summary>

**Definition/Description:** The Primary Alternate Identifier and the Additional Alternate Identifiers (two through Five) uniquely identify either an Alternate Airport or an Alternate Company Route. The determination of whether the content is an Airport Identifier or a Company Route Identifier is accomplished through the Alternate Type field.

**Source/Content:** The content of this field is determined by the customer.

**Used On:** Alternate Records
**Length:** 10 characters max
**Character Type:** Alpha/numeric
</details>

</details>
