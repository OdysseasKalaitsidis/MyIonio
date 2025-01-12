# MyIonio Application

## Overview

**MyIonio** is a Python-based desktop application built with **Tkinter** to provide Ionian University students with an interactive and convenient tool for accessing essential university services, information, and resources. The app combines modern functionalities with an intuitive graphical interface to ensure a seamless user experience.

## Features

### 1. **E-Class Integration**
Quickly navigate to the Ionian University e-Class platform for online course management.

### 2. **Restaurant Menu**
View dining hours and menu updates based on current time, accompanied by dynamic images representing meal periods.

### 3. **Check-In Validation**
Validate if a user is physically located within the university premises using IP and location-based checks.

### 4. **Explore Corfu**
Discover the best spots in Corfu, categorized into:
- Entertainment
- Study Locations
- Food Recommendations

### 5. **Academic Schedule Viewer**
Cycle through a slideshow of academic schedule images to stay updated on classes and events.

### 6. **News and Library Access**
Quick links to the latest university news and library opening hours.

### 7. **Campus Map**
Direct access to a map of the Ionian University campus.

### 8. **Erasmus Support**
Integrated support for Erasmus-related resources and guidance.

## Requirements

### Python Libraries
- `tkinter`: For the graphical user interface.
- `webbrowser`: For opening links in the browser.
- `time`: For real-time dynamic updates.
- `json`: For processing IP and location data.
- `PIL` (Pillow): For enhanced image handling.

### System Requirements
- Python 3.x installed on your machine.
- Internet connection for fetching location-based data and accessing external links.

### File Structure
Ensure the following file paths are updated correctly in the script:
- Images for buttons, labels, and dynamic updates.
- External icons (`icona.ico`) and pictures for specific windows.

## Setup and Usage

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/MyIonio.git
   ```
2. Install required dependencies:
   ```bash
   pip install pillow
   ```
3. Update file paths in the script to match the location of images and icons on your local machine.

4. Run the application:
   ```bash
   python MyIonio.py
   ```

5. Use the interactive interface to explore the various features.

## Folder Structure
```
MyIonio/
│
├── images/
│   ├── icons/
│   ├── restaurant_menu/
│   ├── corfu_spots/
│   ├── schedules/
│   └── ...
│
├── MyIonio.py
└── README.md
```

## Known Issues and Limitations
- Dynamic updates require exact file paths for images.
- Location validation assumes constant IP and geolocation accuracy.
- Only tested on Windows OS with Python 3.x.

## Future Improvements
- Add cross-platform support.
- Improve error handling for missing files or incorrect paths.
- Introduce localization options for non-Greek speakers.
- Enhance the map navigation experience.

## Contributing
Contributions are welcome! If you'd like to add new features, fix bugs, or improve the UI, please:
1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request with detailed explanations.

## License
This project is licensed under the MIT License.
