for i, anchor_project in enumerate(all_projects_data):
    
    for j, negative_project in enumerate(all_projects_data):
        if i == j:
            continue
        # data = {
        #     'English': '',
        #     'Context_Objectives': '',
        #     'Technology/algorithm': '',
        #     'Summarize_the_contents':'',
        #     'Expected features': '',     
        #     'filename': '',     
        # }
        
        # lặp qua từng feature để tạo anchor và negative tương ứng              
        for key in anchor_project.keys():
            if key == 'filename':
                continue
            filename_anchor = anchor_project['filename'] + " "+ key
            filename_negative = negative_project['filename'] + " " + key
            # Tạo bộ ba từ các trường tương ứng
            anchor_text = anchor_project[key]
            negative_text = negative_project[key]
            
            if anchor_text and negative_text and key !='Technology/algorithm':
                triplet_rows.append({
                    'filename_anchor_feature': filename_anchor,
                    'anchor': anchor_text,
                    'positive': '',  # Positive là chính nó
                    'negative': negative_text,  # Negative là dự án khác 
                    'filename_negative_feature': filename_negative
                })
            if anchor_text and negative_text and key =='Technology/algorithm':
                embeddingsAnchor = model.encode(anchor_text)
                embeddingsNegative = model.encode(negative_text)
                similarity_score = model.similarity(embeddingsAnchor, embeddingsNegative)   
                if similarity_score < 0.7:  
                    triplet_rows.append({
                        'filename_anchor_feature': filename_anchor,
                        'anchor': anchor_text,
                        'positive': '',  # Positive là chính nó
                        'negative': negative_text,  # Negative là dự án khác 
                        'filename_negative_feature': filename_negative
                    })  
                else:
                    triplet_rows.append({
                        'filename_anchor_feature': filename_anchor,
                        'anchor': anchor_text,
                        'positive': negative_text,  # Positive là chính nó
                        'negative': '',  # Negative là dự án khác 
                        'filename_negative_feature': filename_negative
                    })  
                    
print(f"Đã tạo {len(triplet_rows)} bộ ba từ dữ liệu trích xuất.")