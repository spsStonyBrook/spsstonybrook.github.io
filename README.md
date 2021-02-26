# Stony Brook SPS Website

## Files

### Pages <HTML5>
- index: Home page
- about: About us and the national organization
- resources: So far empty but resources for students
- schedule: A Google Calendar of events

### Other
- README: Literally this
- LICENSE: Nice fancy license to open-source this
| assets: Files that Pages depend on  
| - | media: images  
| - | ico: files dealing with site manifest or favicon  
| - | style: stylesheets (only styles.css for now)  
| - | postMaker: A super simple md -> HTML converter  
    | - PRE.partial.html: the "beginning" part to sandwich a page with  
    | - POST.partial.html: the "ending" part to sandwich a page with  
    | - example.md: An example input to the tool  
    | - example.html: the output of example.md  
    | - postMaker.py: Script to convert. Usage: `postMaker.py [input\_file] [output\_file]`  

## THINGS THAT NEED TO BE UPDATED YEARLY
- Photos!! When I come back to this website in 4 years, I better not be able to recognize anyone!!!1!!1!!!
- astro.html needs to have the AST 341/346/347/390 "Next Offered" years changed yearly
- Check to make sure all links work

## Conventions

- Push new contributions to the gh-pages branch before merging with master
- When creating new pages, mimic the style of existing ones (ideally copy/paste the <head> and <nav>)
