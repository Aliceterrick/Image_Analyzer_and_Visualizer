namespace Backend.Models;

public class CloudResultDto
{
    public List<DetectionDto> Instances { get; set; } = new();
    public List<DetectionDto> Concepts { get; set; } = new();
}