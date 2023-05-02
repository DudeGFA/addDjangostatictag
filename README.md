# addDjangostatictag

Python scripts that adds Django static tag to:      
- src html attributes       
- href html attributes      
- poster html attributes        
- url() reference       

### Skips lines that reference files on the web and don't require static tag

Usage:
```bash
py add_static_tag.py <inputfilename> <outputfilename>
```

If CLI arguments aren't specified;      
- `inputfilename` defaults to **inputfile.html**        
- `outputfilename` defaults to **outputfile.html**      
