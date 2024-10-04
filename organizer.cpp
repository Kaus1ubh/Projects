#include <iostream>
#include <filesystem>
#include <map>

using namespace std;
namespace fs = std::filesystem;

map<string, string> categories = {
    {".txt", "Documents"}, {".pdf", "Documents"}, {".docx", "Documents"},
    {".jpg", "Images"}, {".png", "Images"}, {".gif", "Images"},
    {".mp4", "Videos"}, {".mkv", "Videos"}, {".avi", "Videos"},
    {".mp3", "Music"}, {".wav", "Music"},
    {".zip", "Archives"}, {".rar", "Archives"}, {".7z", "Archives"}
};

void organizeFiles(const string& path) {
    for (const auto& entry : fs::directory_iterator(path)) {
        if (entry.is_regular_file()) {
            string ext = entry.path().extension().string();
            if (categories.count(ext)) {
                string folder = path + "/" + categories[ext];
                fs::create_directory(folder);
                fs::rename(entry.path(), folder + "/" + entry.path().filename().string());
            }
        }
    }
    cout << "Files organized successfully." << endl;
}

int main() {
    string directory;
    cout << "Enter directory path: ";
    cin >> directory;
    organizeFiles(directory);
    return 0;
}

