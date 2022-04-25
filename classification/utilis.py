from emoji import UNICODE_EMOJI

def remove_emoji(text):
  to_replace = UNICODE_EMOJI["en"]
  result = text
  for x in to_replace:
      result = result.replace(x, "")
  return result