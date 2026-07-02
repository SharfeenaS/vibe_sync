def score_song(image_analysis, song):

    score = 0
    reasons = []

    mood = (image_analysis.get("mood") or "").lower()
    emotions = [e.lower() for e in image_analysis.get("emotions", [])]
    keywords = [k.lower() for k in image_analysis.get("keywords", [])]

    song_mood = (song.get("mood") or "").lower()
    song_keywords = [k.lower() for k in song.get("keywords", [])]
    popularity = song.get("popularity", 0)

    # Mood Match
    if mood == song_mood:
        score += 40
        reasons.append("Mood matched")

    # Keyword Match
    matches = len(set(keywords) & set(song_keywords))
    score += matches * 5

    if matches:
        reasons.append(f"{matches} keyword(s) matched")

    # Emotion Match
    emotion_matches = len(set(emotions) & set(song_keywords))
    score += emotion_matches * 5

    if emotion_matches:
        reasons.append("Emotion matched")

    # Popularity Bonus
    score += popularity // 10

    return score, reasons


def recommend_songs(image_analysis, songs):

    recommendations = []

    for song in songs:

        score, reasons = score_song(image_analysis, song)

        song["score"] = score
        song["reasons"] = reasons

        recommendations.append(song)

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations