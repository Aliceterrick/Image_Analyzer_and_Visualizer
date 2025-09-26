using System.Text.Json;
using Backend.Models;

namespace Backend.Services;

public class ResultsService
{
    private readonly string _resultsDir;
    public ResultsService(IConfiguration cfg)
    {
        _resultsDir = cfg.GetValue<string>("ResultsDirectory")
                      ?? Path.Combine(AppContext.BaseDirectory, "../data/results");
    }

    public IEnumerable<string> ListImageKeys()
        => Directory.Exists(_resultsDir)
            ? Directory.EnumerateFiles(_resultsDir, "*.json")
                       .Select(f => Path.GetFileNameWithoutExtension(f) ?? string.Empty)
            : Enumerable.Empty<string>();

    public ImageResultDto? GetByKey(string key)
    {
        var file = Path.Combine(_resultsDir, key + ".json");
        if (!File.Exists(file)) return null;
        var json = File.ReadAllText(file);
        var dto = JsonSerializer.Deserialize<ImageResultDto>(json,
            new JsonSerializerOptions { PropertyNameCaseInsensitive = true });
        return dto;
    }
}
