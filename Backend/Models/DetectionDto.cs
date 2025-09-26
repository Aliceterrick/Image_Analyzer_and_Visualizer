namespace Backend.Models;

public record DetectionDto(
    string Label,
    double Confidence,
    int[]? Bbox 
);