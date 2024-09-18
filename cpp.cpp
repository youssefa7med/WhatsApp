#include <iostream>
#include <cstdlib>  // for system()

int main() {
    // Command to execute Streamlit for the WhatsApp.py script
    std::string command = "streamlit run \"WhatsApp.py\"";

    // Execute the command in the Windows terminal
    int result = system(command.c_str());

    // Check if the command executed successfully
    if (result == 0) {
        std::cout << "Streamlit started successfully!\n";
    } else {
        std::cout << "Failed to start Streamlit. Error code: " << result << "\n";
    }

    return 0;
}

