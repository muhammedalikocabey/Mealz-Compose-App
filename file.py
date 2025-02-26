import os

def save_android_project_files_to_txt(directory, output_file, included_extensions=None, excluded_patterns=None):
    if included_extensions is None:
        included_extensions = ['.kt', '.java', '.gradle', '.pro']
    
    if excluded_patterns is None:
        excluded_patterns = [
            'ic_', 'build', '.gradle', '.idea', '.git', 'build.gradle', 'gradle-wrapper.properties',
            'gradlew', 'gradlew.bat', 'local.properties', 'settings.gradle', 'app/build', 
            'app/.gradle', 'app/.idea', 'app/.git', 'app/build.gradle', 'es/styles.xml', 
            'navigation.xml', 'drawable', 'ExampleInstrumentedTest', 'ExampleUnitTest', '.xml'
        ]
        
    # XML dosyalarından sadece manifest.xml'leri dahil et
    xml_inclusion_patterns = ['AndroidManifest.xml']

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(directory):
            # Dizinleri kontrol ederek çıkarılacakları ayıkla
            dirs[:] = [d for d in dirs if not any(pattern in d for pattern in excluded_patterns)]
            
            for filename in files:
                file_path = os.path.join(root, filename)
                
                # XML dosyalarını hariç tut, sadece manifest.xml'leri dahil et
                if filename.lower().endswith('.xml') and filename not in xml_inclusion_patterns:
                    continue
                
                # Dosya uzantısını ve desenini kontrol et
                if any(filename.lower().endswith(ext) for ext in included_extensions) or filename in xml_inclusion_patterns:
                    
                    # Dosya yolunu yaz
                    outfile.write(f"File Path: {file_path}\n")
                    
                    # Package bilgisini ekle (.kt veya .java dosyaları için)
                    if filename.lower().endswith(('.kt', '.java')):
                        package_name = None
                        try:
                            with open(file_path, 'r', encoding='utf-8') as infile:
                                for line in infile:
                                    if line.strip().startswith("package"):
                                        package_name = line.strip()
                                        break
                        except Exception as e:
                            outfile.write(f"Error reading file: {str(e)}\n")

                        if package_name:
                            outfile.write(f"{package_name}\n")
                    
                    outfile.write("-" * 40 + "\n")
                    
                    # Dosya içeriğini yaz
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                            outfile.write(content + "\n")
                    except Exception as e:
                        outfile.write(f"Error reading file: {str(e)}\n")
                    
                    outfile.write("=" * 40 + "\n\n")

if __name__ == "__main__":
    # Script'in çalıştığı klasörü alır
    directory = os.path.dirname(os.path.abspath(__file__))
    
    # Çıktı dosyasının adı (script'in çalıştığı dizinde)
    output_file = os.path.join(directory, "android_project_files.txt")
    
    save_android_project_files_to_txt(directory, output_file)
    print(f"All relevant code files' contents have been saved to {output_file}")
