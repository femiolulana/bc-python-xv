class NotesApplication(object):
  def __init__(self, author):
    self.author = author
    self.notes_list = []
  
  def create(self, note_content):
    self.note_content = note_content
    self.notes_list.append(note_content)
    return self
    
  def list(self):
    for i in range(len(self.notes_list)):
      print ('Note ID: {}'.format(i))
      print ('{}'.format(self.notes_list[i]))
      print ('By Author {}'.format(self.author))
  
  def get(self, note_id):
    self.content = self.notes_list[note_id]
    return self.content

  def search(self, search_text):
    add = "Showing results for search \"[<"+search_text+">]\""
    for i in self.notes_list:
      if search_text in i:
        note_content = self.notes_list.index(i)
        add += "\n Note ID: %d \n %s \n By Author  %s"%(note_content, i, self.author)
    a = str(add)
    print (a)
    
  def delete(self, note_id):
    del self.notes_list[note_id]
    
  def edit(self, note_id, new_content):
    self.notes_list[note_id] = new_content
