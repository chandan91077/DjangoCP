# Django ORM & Shell Commands - Quick Reference

## Table of Contents
1. [Entering Python Shell](#entering-python-shell)
2. [Basic Queries](#basic-queries)
3. [Creating Records](#creating-records)
4. [Retrieving Data](#retrieving-data)
5. [Updating Records](#updating-records)
6. [Deleting Records](#deleting-records)
7. [Dictionary vs Model Instance](#dictionary-vs-model-instance)
8. [Limiting Results](#limiting-results)
9. [Common Errors](#common-errors)

---

## Entering Python Shell

```bash
# Windows
python manage.py shell

# Or
py manage.py shell
```

**Expected Output:**
```
Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37)
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
```

---

## Basic Queries

### Import Model
```python
from contact.models import Person
```

### Get All Records
```python
Person.objects.all()
# Output: <QuerySet [<person: John Doe>, <person: shyam>]>
```

### Count Records
```python
Person.objects.count()
# Output: 2
```

---

## Creating Records

### Method 1: Using create()
```python
Person.objects.create(
    name="John Doe",
    email="john@example.com",
    subject="Hello",
    message="This is my message"
)
```

### Method 2: Using save()
```python
p = Person()
p.name = "John Doe"
p.email = "john@example.com"
p.subject = "Hello"
p.message = "This is my message"
p.save()
```

---

## Retrieving Data

### Get Single Record by ID
```python
# Returns Model Instance
p = Person.objects.get(id=2)
# Output: <person: shyam>
```

### Get as Dictionary (Values)
```python
# Returns Dictionary - READ ONLY
x = Person.objects.all().values().get(id=2)
# Output: {'id': 2, 'name': 'shyam', 'email': 'shyam@example.com', ...}
```

### Access Dictionary Fields
```python
x['name']      # 'shyam'
x['email']     # 'shyam@example.com'
x['subject']   # 'Test Subject heklo'
x['message']   # 'This is a test message!'
```

### Access Model Instance Attributes
```python
p.name      # 'shyam'
p.email     # 'shyam@example.com'
p.subject   # 'Test Subject heklo'
p.message   # 'This is a test message!'
```

---

## Updating Records

### Update Model Instance (Saves to DB)
```python
# Step 1: Get the record
p = Person.objects.get(id=2)

# Step 2: Update field
p.name = 'raheshyam'

# Step 3: Save to database
p.save()
```

### Update Multiple Fields at Once
```python
Person.objects.filter(id=2).update(
    name='raheshyam',
    subject='New Subject'
)
# No .save() needed!
```

### Update from Dictionary to Database
```python
# Dictionary (temporary, doesn't save)
x = {'id': 2, 'name': 'raheshyam', 'email': 'shyam@example.com', ...}

# Convert to model and save
p = Person.objects.get(id=x['id'])
p.name = x['name']
p.email = x['email']
p.subject = x['subject']
p.message = x['message']
p.save()
```

---

## Deleting Records

### Delete Single Record
```python
p = Person.objects.get(id=2)
p.delete()
# Output: (1, {'contact.Person': 1})
```

### Delete Without Variable
```python
Person.objects.get(id=2).delete()
```

### Delete Using Filter (Safer)
```python
Person.objects.filter(id=2).delete()
```

### Delete All Records (⚠️ DANGER)
```python
Person.objects.all().delete()
```

---

## Dictionary vs Model Instance

| Feature | Dictionary (`.values()`) | Model Instance (`.get()`) |
|---------|-------------------------|---------------------------|
| Syntax | `x['name']` | `p.name` |
| Can modify DB | ❌ NO | ✅ YES |
| Has `.save()` | ❌ NO | ✅ YES |
| Has `.delete()` | ❌ NO | ✅ YES |
| Type | `dict` | `Person` model |
| Usage | Read-only data display | Full CRUD operations |

### Important Rule
> **Dictionaries are temporary copies. Only Model Instances can save to database!**

---

## Limiting Results

### Get Last 2 Records (Newest First)
```python
Person.objects.all().order_by('-id')[:2]
```

### In Template (Slice)
```html
{% for response in responses|slice:":2" %}
```

### In View
```python
def response_list(request):
    responses = Person.objects.all().order_by('-id')[:2]
    return render(request, 'contact/response.html', {'responses': responses})
```

---

## Common Errors

### Error: `'from' keyword not supported`
**Cause:** Running Python code in PowerShell instead of Python shell

**Fix:**
```bash
python manage.py shell
# Then run Python code
```

### Error: `'dict' object has no attribute 'name'`
**Cause:** Trying to use model attribute syntax on dictionary

**Fix:**
```python
# Wrong
x.name = 'raheshyam'

# Right
x['name'] = 'raheshyam'

# Or use model instance
p = Person.objects.get(id=2)
p.name = 'raheshyam'
p.save()
```

---

## Quick Command Reference

| Action | Command |
|--------|---------|
| Start shell | `python manage.py shell` |
| Run server | `python manage.py runserver` |
| Make migrations | `python manage.py makemigrations` |
| Apply migrations | `python manage.py migrate` |
| Show SQL | `python manage.py sqlmigrate app_name 0001` |

---

## Template Example (response.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Responses</title>
</head>
<body>
    <h1>All Responses</h1>

    {% if responses %}
        {% for response in responses %}
            <div>
                <h2>Response #{{ forloop.counter }}</h2>
                <p>Name: {{ response.name }}</p>
                <p>Email: {{ response.email }}</p>
                <p>Subject: {{ response.subject }}</p>
                <p>Message: {{ response.message }}</p>
                <hr>
            </div>
        {% endfor %}
    {% else %}
        <p>No responses found.</p>
    {% endif %}
</body>
</html>
```

---

## Model Definition (models.py)

```python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
```

---

*Created for memorization purposes* 📝
