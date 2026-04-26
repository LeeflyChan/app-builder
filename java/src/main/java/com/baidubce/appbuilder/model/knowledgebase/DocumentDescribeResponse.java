package com.baidubce.appbuilder.model.knowledgebase;

import java.util.List;
import java.util.Map;

public class DocumentDescribeResponse {
    private String documentId;
    private String name;
    private String createdAt;
    private String status;
    private Meta meta;
    private EnhanceStatus enhanceStatus;
    private EnhanceStatus graphTaskStatus;

    public String getId() {
        return documentId;
    }

    public void setId(String id) {
        this.documentId = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
    }

    public String getDisplayStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public Meta getMeta() {
        return meta;
    }

    public void setMeta(Meta meta) {
        this.meta = meta;
    }

    public EnhanceStatus getEnhanceStatus() {
        return enhanceStatus;
    }

    public void setEnhanceStatus(EnhanceStatus enhanceStatus) {
        this.enhanceStatus = enhanceStatus;
    }

    public EnhanceStatus getGraphTaskStatus() {
        return graphTaskStatus;
    }

    public void setGraphTaskStatus(EnhanceStatus graphTaskStatus) {
        this.graphTaskStatus = graphTaskStatus;
    }

    public static class Meta {
        private String source;
        private Integer wordCount;
        private String mimeType;
        private String url;
        private Integer fileSize;
        private List<Map<String, Object>> tags;


        public String getSource() {
            return source;
        }

        public void setSource(String source) {
            this.source = source;
        }

        public String getUrl() {
            return url;
        }

        public void setUrl(String url) {
            this.url = url;
        }
        
        public String getMimeType() {
            return mimeType;
        }

        public void setMimeType(String mimeType) {
            this.mimeType = mimeType;
        }

        public Integer getFileSize() {
            return fileSize;
        }

        public void setFileSize(Integer fileSize) {
            this.fileSize = fileSize;
        }
        public Integer getWordCount() {
            return wordCount;
        }
        public void setWordCount(Integer wordCount) {
            this.wordCount = wordCount;
        }
        public List<Map<String, Object>> getTags() {
            return tags;
        }
        public void setTags(List<Map<String, Object>> tags) {
            this.tags = tags;
        }
    }

    public static class EnhanceStatus {
        private String status;
        private String message;

        public String getStatus() {
            return status;
        }

        public void setStatus(String status) {
            this.status = status;
        }

        public String getMessage() {
            return message;
        }

        public void setMessage(String message) {
            this.message = message;
        }
    }
}
